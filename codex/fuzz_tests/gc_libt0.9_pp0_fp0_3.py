import gc, weakref
from time import time as global_clock
from wdata.ThreadQueue import ThreadQueue
from wdata.SimpleThr import SimpleThr

from logging import error, debug
from ganeti import constants, opcodes
from ganeti import errors
from ganeti import utils
from ganeti import ssconf
from ganeti import compat
from ganeti import runtime
from ganeti.rpc.client import RpcResult, BootstrapRunner
from ganeti import job
from ganeti import backend
from ganeti import node as node_mod


class _FakeContext(object):
  """Fake context.

  This represents a dummy context object, as used by L{ssconf}.

  """
  def __init__(self, vg_name, cluster_name):
    self.vg_name = vg_name
    self.cluster_name = cluster_name


class QueueManager(object):
  """Watcher queue manager.

  This class is responsible for handling the internal and the RPC queues. The
  events will be handled
