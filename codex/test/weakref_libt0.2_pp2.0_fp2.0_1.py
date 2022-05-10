import weakref

from . import _core
from . import _util
from . import _errors
from . import _types
from . import _constants
from . import _compat
from . import _compat_pickle
from . import _compat_collections_abc

from . import _lazy_import
_lazy_import.lazy_module("_cython_utils")
_lazy_import.lazy_module("_cython_utils_importers")
_lazy_import.lazy_module("_cython_utils_memoryview")
_lazy_import.lazy_module("_cython_utils_buffer")
_lazy_import.lazy_module("_cython_utils_numpy_support")
_lazy_import.lazy_module("_cython_utils_numpy_support_importers")
_lazy_import.lazy_module("_cython_utils_numpy_support_memoryview")
