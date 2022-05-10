import weakref
import os

__all__ = ["Node", "ArrayNode", "ValueNode", "ListNode", "DictNode", "RemoteNode", "RemoteValueNode", "RemoteListNode", "RemoteDictNode", "RemoteRootNode", ]

def _values_to_nodes(obj):
    if isinstance(obj, Node):
        return obj
    elif isinstance(obj, (tuple, list)):
        return ListNode([_values_to_nodes(o) for o in obj])
    elif isinstance(obj, dict):
        return DictNode({k: _values_to_nodes(v) for k, v in obj.items()})
    else:
        return ValueNode(obj)

class Node(object):
    _value = None
    _tags = None

    def __init__(self, tags=None):
        self._tags = tags
        self._handlers = []


    def _handle_change(self, sender, change):
        for handler in self._handlers:
            handler(sender, change)


   
