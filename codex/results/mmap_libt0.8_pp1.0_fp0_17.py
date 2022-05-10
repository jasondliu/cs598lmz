import mmap
from PIL import Image
from collections import namedtuple
from typing import Tuple, Iterator, List
from .bounds import Bounds
from .node import Node
from .block import Block
from .pointers import Reader


def make_reader(filename:str) -> Reader:
    """Make a Reader out of a filename"""
    return mmap.mmap(os.open(filename, os.O_RDONLY), 0, access=mmap.ACCESS_READ)


def read_bounds(reader:Reader) -> Bounds:
    """Read bounds from Reader"""
    minx, miny, maxx, maxy = struct.unpack("<llll", reader.read(16))
    return Bounds(minx, miny, maxx, maxy)


def read_node(reader:Reader, bounds:Bounds, recursion:int) -> Node:
    """Read a Node from Reader"""
    if recursion > 32:
        raise Exception("recursion > 32")
    node = Node()
    node.bounds = bounds
    node.nodetype =
