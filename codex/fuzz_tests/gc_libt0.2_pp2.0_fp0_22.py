import gc, weakref

from . import _pywrap_tensorflow
from . import errors
from . import pywrap_tensorflow
from . import tensor_shape
from . import tensor_util
from . import types
from . import util
from .util import compat
from .util import nest
from .util import tf_contextlib
from .util.deprecation import deprecated
from .util.tf_decorator import classproperty
from .util.tf_export import tf_export
from .util.tf_inspect import getfullargspec as tf_inspect_getfullargspec
from .util.tf_inspect import getargspec as tf_inspect_getargspec
from .util.tf_inspect import getcallargs as tf_inspect_getcallargs
from .util.tf_inspect import getsource as tf_inspect_getsource
from .util.tf_inspect import isclass as tf_inspect_isclass
from .util.tf_inspect import isgeneratorfunction as tf_inspect_isgeneratorfunction
from .util.tf_inspect import ismethod as tf
