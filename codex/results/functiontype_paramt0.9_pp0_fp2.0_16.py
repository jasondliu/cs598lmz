from types import FunctionType
list(FunctionType(FunctionType.__code__,"FunctionType").__closure__)


#%%

from __future__ import annotations
import abc
from collections import namedtuple
from typing import Callable
from typing import Tuple
from typing import Union
Point = namedtuple("Point", "x, y")

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    def __iter__(self):
        for point in (self.p1, self.p2):
            yield point
    def __eq__(self, other: Line) -> bool:
        return all(p1 == p2 for p1, p2 in zip(self, other))

class Rectangle:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    def __iter__(self):
        yield from Line(self.p1, Point(self.p2.x, self.p1.
