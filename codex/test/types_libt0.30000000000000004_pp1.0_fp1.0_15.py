import types
types.FunctionType = types.BuiltinFunctionType

from . import _pywrap_tensorflow as tf
from . import _pywrap_tensorflow_internal as tf_int
from . import _pywrap_utils
from . import _pywrap_tf_session
from . import _pywrap_tf_session_helper
from . import _pywrap_tf_session_target
from . import _pywrap_tf_status
from . import _pywrap_tf_tensor
