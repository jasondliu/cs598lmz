import weakref

from . import _util
from . import _pywrap_tensorflow_internal as _pywrap_utils
from . import errors_impl
from . import pywrap_tensorflow
from . import tensor_shape
from . import tensor_util
from .framework import dtypes
from .framework import ops
from .framework import tensor_shape
from .ops import gen_array_ops
from .util import compat
from .util import deprecation
from .util import nest
from .util import tf_contextlib
from .util.tf_export import tf_export


# pylint: disable=protected-access
_USE_C_API = pywrap_tensorflow.TFE_Py_TensorHandleUsedByAutoTuner()
# pylint: enable=protected-access


def _make_handle(device, op_name, output_num, dtype, shape, name):
  """Creates a handle for the given tensor."""
