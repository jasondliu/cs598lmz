import gc, weakref
from collections import deque

from .memory import Memory
from .data import (
    Node, HumanControl, Action,
    ActionType, NodeLink, NodeValue,
    NodeLinkValue, NodeLinkType, NodeLinkState,
    NodeType, NodeState, NodeValueType, NodeLinkValueType,
    ActionState,
)
from .data import (
    NodeValueData, NodeLinkValueData,
    NodeValueDataList, NodeLinkValueDataList,
    NodeValueDataDict, NodeLinkValueDataDict,
)
from .data import (
    NodeValueList, NodeLinkValueList,
    NodeValueDict, NodeLinkValueDict,
)
from .sequence import Sequence
from .event import Event


class MemoryManager(object):
    def __init__(self, memory=None, parent=None):
        self.parent = parent
        self.memory = memory if memory is not None else Memory(self)
        self.current_sequence = None
        self.current_node = None
        self.current_link = None
        self.current_link_index = 0
