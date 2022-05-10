import gc, weakref

# from . import error
from . import _build
from . import _function
from . import _registry
from . import _util
from . import _wrap

__all__ = [
    'register_function',
    'function',
    'Function',
    'ConcreteFunction',
    '_get_concrete_function_garbage_collector',
]


def _get_concrete_function_garbage_collector():
  """Returns the garbage collector used by ConcreteFunction."""
  if not _function.USE_DEFERRED_CONCRETE_FUNCTIONS:
    return None
  if ConcreteFunction._garbage_collector is None:
    ConcreteFunction._garbage_collector = _GarbageCollector()
  return ConcreteFunction._garbage_collector


def _get_concrete_function_list():
  """Returns the list of ConcreteFunctions to be garbage collected."""
  return _get_concrete_function_garbage_collector().concrete_functions


def register_function(f, name=None):

