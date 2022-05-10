import types
types.ModuleType.__dict__.__setitem__('__path__', [])

try:
    from . import _pywrap_tensorflow_internal
except ImportError:
    pass
from . import _pywrap_tensorflow_internal  # pylint: disable=redefined-builtin, unused-import
from tensorflow.python.util import module_wrapper as _module_wrapper
_pywrap_tensorflow_internal = _module_wrapper.module_wrapper(_pywrap_tensorflow_internal)


from tensorflow.python.util.lazy_loader import LazyLoader
_op_def_registry = LazyLoader("_op_def_registry")
_op_def_lib = LazyLoader("_op_def_lib")


def _InitOpDefLibrary():
  op_list = _op_def_lib.op_list_as_py_val()
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_
