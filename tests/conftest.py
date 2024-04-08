"""
tests.conftest
==============
"""

from __future__ import annotations

from pathlib import Path

import pytest

from . import FixturePatchArgv


@pytest.fixture(name="environment", autouse=True)
def fixture_environment(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Prepare environment for testing.

    :param monkeypatch: Mock patch environment and attributes.
    :param tmp_path: Create and return temporary directory.
    """
    monkeypatch.chdir(tmp_path)


@pytest.fixture(name="patch_argv")
def fixture_patch_argv(monkeypatch: pytest.MonkeyPatch) -> FixturePatchArgv:
    """Patch commandline arguments.

    :param monkeypatch: Mock patch environment and attributes.
    :return: Function for using this fixture.
    """

    def _patch_argv(*args: str) -> None:
        monkeypatch.setattr("sys.argv", [str(a) for a in args])

    return _patch_argv
