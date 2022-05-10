import weakref

from . import _pywrap_tensorflow as tf_session
from . import errors
from . import pywrap_tensorflow
from . import tensor_shape
from . import tensor_util
from . import types
from . import version
from .util import compat
from .util import nest
from .util import tf_contextlib
from .util import tf_decorator
from .util import tf_inspect
from .util import tf_should_use
from .util.deprecation import deprecated
from .util.nest import map_structure
from .util.nest import pack_sequence_as
from .util.nest import register_composites
from .util.nest import register_pytype
from .util.nest import register_pytype_for_composites
from .util.nest import register_pytype_for_name
from .util.nest import register_pytype_for_tensor
from .util.nest import register_pytype_for_tensor_and_indexed_slices
from .util.nest import register_py
