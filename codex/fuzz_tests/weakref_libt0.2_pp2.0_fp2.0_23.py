import weakref

from . import _pywrap_tensorflow as tf_session
from . import errors_impl
from . import session_ops
from . import session_state
from . import tensor_util
from . import util
from .framework import dtypes
from .framework import ops
from .framework import tensor_shape
from .framework import types
from .util import compat
from .util import nest
from .util import portpicker
from .util.device_name_utils import canonicalize
from .util.device_name_utils import canonicalize_device_name
from .util.device_name_utils import parse_device_name
from .util.device_name_utils import parse_device_name_or_function
from .util.device_name_utils import split_device_name
from .util.nest import map_structure
from .util.nest import pack_sequence_as
from .util.nest import pack_sequence_as_nested_structure
from .util.nest import pack_sequence_as_tuple
from .util.nest import pack_sequence_as_t
