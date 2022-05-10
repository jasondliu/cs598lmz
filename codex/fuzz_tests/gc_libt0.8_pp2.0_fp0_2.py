import gc, weakref
from . import _nodegroup
from . import _libgeode as _lgeode

class NodeGroup(_nodegroup.NodeGroup):
  def __init__(self, *args):
    _nodegroup.NodeGroup.__init__(self, *args)

  def __del__(self):
    if self and self.initialized_:
      self.clear()
    _nodegroup.NodeGroup.__del__(self)


class NodeCache(object):
  # A cache of nodes, kept both in a Python dict and in a NodeGroup.

  # The python weakref machinery could handle everything here, except that
  # nodegroup doesn't provide a place to store a key.  This is a reasonable
  # solultion, but the time complexity isn't quite right.  It'll do for now.

  def __init__(self):
    self.group = NodeGroup()
    self.group.clear()
    self.dict = {}

  def node_to_key(self, n):
    n = n.id()
    n ^= (n >> 30) * 0x
