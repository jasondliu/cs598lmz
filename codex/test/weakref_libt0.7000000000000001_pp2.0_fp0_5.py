import weakref

from . import _binding
from . import _binding_utils
from . import _libs
from . import _utils
from . import exceptions
from . import resources
from . import types
from . import _types

from .types import _Type
from .resources import Resource

def _apply_configs(configs):
  for config in configs:
    config()

class Context(_binding_utils.with_metaclass(types.SingletonType, object)):
  """
  A TensorFlow Context.

  A context object is used to store the context (i.e., state) of the TensorFlow
  API. The context can be used as a singleton, or it can be used as a
  contextmanager in a with statement.
  """

  # TensorFlow API version.
  API_VERSION = "0.12.0"

  # Static attributes.
  _graph = None
  _current_device_function = None
  _current_device_function_stack = []
  _current_device = None
  _current_device_stack = []
  _
