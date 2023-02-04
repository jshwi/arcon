"""
tests._test
===========
"""
from __future__ import annotations

import typing as t
from pathlib import Path

import pytest
import tomli_w

import arcon
from arcon import ArgumentParser

from . import (
    DICT,
    LIST,
    NAME,
    TOML,
    TOOL,
    VERSION,
    FixturePatchArgv,
    long,
    short,
    string,
)


def test_version(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test ``arcon.__version__``.

    :param monkeypatch: Mock patch environment and attributes.
    """
    monkeypatch.setattr("arcon.__version__", VERSION)
    assert arcon.__version__ == VERSION


@pytest.mark.parametrize(
    "config,args,expected",
    [
        (
            {TOOL: {NAME: {LIST: []}}},
            [NAME, long.list, f"{string[1]},{string[2]},{string[3]}"],
            [string[1], string[2], string[3]],
        ),
        (
            {TOOL: {NAME: {LIST: [string[4]]}}},
            [NAME, long.list, f"{string[1]},{string[2]},{string[3]}"],
            [string[1], string[2], string[3], string[4]],
        ),
    ],
    ids=["empty-conf", "with-conf"],
)
def test_list_parser(
    patch_argv: FixturePatchArgv,
    config: dict[str, t.Any],
    args: tuple[str, ...],
    expected: list[str],
) -> None:
    """Test ``arcon.ArgumentParser.add_list_args``.

    :param patch_argv: Patch commandline arguments.
    :param config: Object to write to pyproject.toml.
    :param args: Arguments to pass to commandline.
    :param expected: Expected result.
    """
    Path(TOML).write_text(tomli_w.dumps(config), encoding="utf-8")
    patch_argv(*args)
    parser = ArgumentParser(VERSION)
    parser.add_list_argument(short.list, long.list)
    namespace = parser.parse_args()
    assert namespace.list == expected


@pytest.mark.parametrize(
    "config,args,expected",
    [
        (
            {TOOL: {NAME: {DICT: {}}}},
            [
                NAME,
                long.dict,
                f"{string[0]}={string[1]},{string[2]},{string[3]}",
            ],
            {string[0]: [string[1], string[2], string[3]]},
        ),
        (
            {TOOL: {NAME: {DICT: {string[0]: [string[4]]}}}},
            [
                NAME,
                long.dict,
                f"{string[0]}={string[1]},{string[2]},{string[3]}",
            ],
            {string[0]: [string[1], string[2], string[3], string[4]]},
        ),
        (
            {TOOL: {NAME: {DICT: {string[1]: [string[1]]}}}},
            [
                NAME,
                long.dict,
                f"{string[0]}={string[1]},{string[2]},{string[3]}",
            ],
            {
                string[0]: [string[1], string[2], string[3]],
                string[1]: [string[1]],
            },
        ),
    ],
    ids=["empty-conf", "add-to-obj", "add-new-obj"],
)
def test_dict_parser(
    patch_argv: FixturePatchArgv,
    config: dict[str, t.Any],
    args: tuple[dict[str, t.Any], ...],
    expected: list[str],
) -> None:
    """Test ``arcon.ArgumentParser.add_dict_args``.

    :param patch_argv: Patch commandline arguments.
    :param config: Object to write to pyproject.toml.
    :param args: Arguments to pass to commandline.
    :param expected: Expected result.
    """
    Path(TOML).write_text(tomli_w.dumps(config), encoding="utf-8")
    patch_argv(*args)
    parser = ArgumentParser(VERSION)
    parser.add_dict_argument(short.dict, long.dict)
    namespace = parser.parse_args()
    assert namespace.dict == expected


def test_dict_value_error(patch_argv: FixturePatchArgv) -> None:
    """Test ``arcon.ArgumentParser.add_dict_args`` with invalid arg.

    :param patch_argv: Patch commandline arguments.
    """
    patch_argv(NAME, long.dict, string[0])
    parser = ArgumentParser(VERSION)
    parser.add_dict_argument(short.dict, long.dict)
    namespace = parser.parse_args()
    assert namespace.dict == {}


def test_no_toml(patch_argv: FixturePatchArgv) -> None:
    """Test ``arcon.ArgumentParser`` with no config.

    :param patch_argv: Patch commandline arguments.
    """
    patch_argv(NAME, long.arg)
    parser = ArgumentParser(VERSION)
    parser.add_argument(short.arg, long.arg, action="store_true")
    namespace = parser.parse_args()
    assert namespace.arg


def test_regular_flags(patch_argv: FixturePatchArgv) -> None:
    """Test ``arcon.ArgumentParser`` uses proper slug.

    :param patch_argv: Patch commandline arguments.
    """
    config = {TOOL: {NAME: {"this-flag": True}}}
    Path(TOML).write_text(tomli_w.dumps(config), encoding="utf-8")
    patch_argv(NAME)
    parser = ArgumentParser(VERSION)
    parser.add_argument(short.this_flag, long.this_flag, action="store_true")
    namespace = parser.parse_args()
    assert namespace.this_flag is True
