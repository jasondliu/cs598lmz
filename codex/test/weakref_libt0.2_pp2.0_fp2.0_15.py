import weakref

from . import _util
from . import _pywrap_tensorflow_internal
from . import errors_impl
from . import pywrap_tensorflow
from . import tensor_shape
from . import tensor_util
from . import type_spec
from . import version
from .util.tf_export import tf_export
from .util.tf_inspect import getfullargspec
from .util.tf_inspect import getmodule
from .util.tf_inspect import isclass
from .util.tf_inspect import isfunction
from .util.tf_inspect import ismethod
from .util.tf_inspect import ismodule
from .util.tf_inspect import ismethoddescriptor
from .util.tf_inspect import isroutine
from .util.tf_inspect import unwrap


# pylint: disable=protected-access
_TF_COMPATIBLE_TAG = "tf._api_internal._TF_COMPATIBLE_TAG"
