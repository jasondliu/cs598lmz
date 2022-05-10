import gc, weakref

from . import _pywrap_tensorflow as tf_session
from . import errors
from . import pywrap_tensorflow
from . import session_ops
from . import util
from . import variable_scope
from .framework import ops
from .util import compat
from .util import deprecation
from .util import nest
from .util import portpicker
from .util import protobuf
from .util import tf_contextlib
from .util import tf_decorator
from .util import tf_inspect
from .util import tf_stack

# pylint: disable=g-bad-import-order
from tensorflow.python.util import compat as compat_lib
from tensorflow.python.util import tf_should_use
from tensorflow.python.util.tf_export import tf_export
# pylint: enable=g-bad-import-order

# pylint: disable=protected-access
_USE_C_API = tf_should_use._USE_C_API
# pylint: enable=protected-access

# Default value for the
