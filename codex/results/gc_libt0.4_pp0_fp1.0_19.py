import gc, weakref
import sys

from . import _pywrap_tensorflow_internal as c_api
from . import pywrap_tensorflow
from . import session_options_pb2
from . import tensor_shape_pb2
from . import types_pb2
from . import variable_pb2
from .framework import attr_value_pb2
from .framework import device_attributes_pb2
from .framework import function_pb2
from .framework import graph_pb2
from .framework import node_def_pb2
from .framework import op_def_pb2
from .framework import op_def_util
from .framework import versions_pb2
from .util import compat as _compat
from .util import nest as _nest
from .util import portpicker
from .util import protobuf
from .util import proto_util

# pylint: disable=protected-access
_TF_VERSION = versions_pb2.VersionDef(
    producer=22,
    min_consumer=0,
    bad_consumers=[],
    version=versions_pb2.VersionDef.
