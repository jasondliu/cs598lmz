import mmap

from collections import defaultdict
from itertools import count
from networkx import DiGraph, topological_sort
from networkx.drawing.nx_pydot import write_dot
from typing import Any, DefaultDict, Dict, List, Optional, Set

from . import util


class Graph:

    def __init__(self, verbose=False, **kwargs):
        self.verbose = verbose
        self.nodes = DiGraph(**kwargs)
        self.nodes.graph['graph'] = {'rankdir': 'LR'}
        self.node_ids = {}  # type: Dict[str, int]
        self.node_count = 0
        self.marked = defaultdict(bool)  # type: DefaultDict[str, bool]
        self.contents = {}  # type: Dict[str, Any]

    def add_node(self, name, label=None, shape='box', color='black'):
        if name in self.nodes:
            raise ValueError('duplicate node name: {}'.format
