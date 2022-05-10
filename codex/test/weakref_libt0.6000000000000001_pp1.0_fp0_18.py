import weakref

from . import _api
from . import _tensor
from . import _types
from . import _typing
from . import _util
from . import compat
from . import config
from . import py_builtins
from . import py_collections
from . import py_exceptions
from . import py_random
from . import py_string
from . import py_struct
from . import py_utils
from . import pytree
from . import trace
from . import tracing
from .pytracer import PyTracer
from . import xla
from . import xla_bridge
from . import xla_client
from . import xla_extension
from . import xla_sharding


# TODO(mattjj): remove this once we have a better way to deal with
# dynamic control flow
_control_flow_context = None
_xla_bridge_context = None


def _check_control_flow_context():
  global _control_flow_context
  if _control_flow_context is None:
    raise RuntimeError("No control flow context active")
  return _
