from __future__ import annotations
from typing import List, Dict, Union, TypedDict, Optional


class NestedDict(TypedDict):
    number: int
    string: str
    maybe: str


class SameNestedDict(TypedDict):
    number: int
    string: str
    maybe: None


class Root(TypedDict):
    nested_dict: NestedDict
    same_nested_dict: SameNestedDict
