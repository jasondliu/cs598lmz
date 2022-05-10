import weakref

from . import _pywrap_tensorflow_internal as tf_inspect
from . import compat as _compat
from .util import _nest

_FORWARD_REF_ATTRIBUTE = "_forward_ref_"


class _ForwardRef(object):
  """Wraps an object that is a forward reference.

  A forward reference is an object that is not defined yet, but will be
  defined later on. For example, when defining a class Foo that has
  a member bar, bar is a forward reference to class Bar (assuming Bar
  has not been defined yet).

  _ForwardRef is used to wrap objects that are forward references.
  It can be unwrapped to get the underlying object, if it has been
  defined. If it has not been defined yet, it raises an error.
  """

  def __init__(self, arg):
    """Creates a new _ForwardRef.

    Args:
      arg: the object that is a forward reference.
    """
    self._arg = arg
    self._computed_arg = None

  def _compute_arg
