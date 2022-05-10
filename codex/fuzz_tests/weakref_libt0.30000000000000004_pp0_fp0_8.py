import weakref

from . import _pywrap_tensorflow_internal as _internal
from . import pywrap_tensorflow
from . import util
from .util import compat
from .util import deprecation
from .util import nest
from .util import tf_contextlib
from .util.tf_export import tf_export


# pylint: disable=protected-access
_TF_VERSION = pywrap_tensorflow.TF_Version()
_IS_TF_1 = _TF_VERSION.is_tf1
_IS_TF_2 = _TF_VERSION.is_tf2
_IS_TF_2_BEHAVIOR = _TF_VERSION.is_tf2_behavior
_IS_TF_2_BEHAVIOR_ENABLED = _IS_TF_2_BEHAVIOR and not _IS_TF_1
_IS_TF_2_GRAPH_ENABLED = _IS_TF_2 and not _IS_TF_1
_IS_TF_2_ENABLED = _IS_TF_2 and not _IS_TF_1
_IS_
