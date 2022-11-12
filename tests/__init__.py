"""
tests
=====

Test package for ``arcon``.
"""
from __future__ import annotations

import typing as _t
from pathlib import Path as _Path

from templatest.utils import VarPrefix as _VarPrefix
from templatest.utils import VarSeq as _VarSeq

FixturePatchArgv = _t.Callable[..., None]

short = _VarPrefix("-")
long = _VarPrefix("--", slug="-")
string = _VarSeq("string")

NAME = "project"
TOML = "pyproject.toml"
VERSION = "0.1.0"
TOOL = "tool"
LIST = "list"
DICT = "dict"
