import select
import sys
from typing import Deque, Dict, List, NamedTuple, Tuple
import warnings

import attr

from . import i3
from . import run_i3_test


@attr.s(auto_attribs=True)
class TestDraw(NamedTuple):
    output: str
    x: int
    y: int
    width: int
    height: int


class TestDestroy(NamedTuple):
    pass


class TestWindow(NamedTuple):
    x: int
    y: int
    width: int
    height: int


def run_test(root, test_name: str, argv: List[str] = None) -> int:
    """
    Execute a test i3bar plugin and return a tuple of the STDOUT output and
    the yielded events.

    """
    name = os.path.join(root, 'test_i3bar.py')
    output = subprocess.check_output([sys.executable, name, test_name])
