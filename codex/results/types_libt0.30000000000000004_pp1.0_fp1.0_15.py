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
from . import _pywrap_tf_tensor_util
from . import _pywrap_tf_types
from . import _pywrap_tf_variable
from . import _pywrap_tf_version
from . import _pywrap_tf_xla
from . import _pywrap_tf_xla_client
from . import _pywrap_tf_xla_ops
from . import _pywrap_tf_xla_py
from . import _pywrap_tf_xla_test
from . import _pywrap_tf_xla_tfcompile
from . import _pywrap_tf_xla_util
