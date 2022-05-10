import types
types.ModuleType('_pywrap_tensorflow')
import _pywrap_tensorflow
from tensorflow.python.util import compat
from tensorflow.python.platform import self_check
from tensorflow.python.platform import flags as tf_flags
from tensorflow.python.platform import app
from tensorflow.python.platform import gfile
from tensorflow.python.platform import resource_loader
from tensorflow.python.platform import sysconfig
from tensorflow.python.platform import tf_logging as logging
from tensorflow.python.util import deprecation
from tensorflow.python.util.tf_export import tf_export
from tensorflow.core.framework import graph_pb2
from tensorflow.core.framework import node_def_pb2
from tensorflow.core.framework import attr_value_pb2
from tensorflow.core.framework import tensor_pb2
from tensorflow.core.framework import types_pb2
from tensorflow.core.framework import versions_pb2
