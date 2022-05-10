import gc, weakref
import warnings

from . import _util
from . import globals
from . import core
from . import _core
from . import config
from .core import *
from .core import _duckarray_ops
from .core import _duckarray_ufuncs

from .core import _shim_ns_dict
from .core import _gloo_flags_ns_dict
from .core import _gloo_ns_dict
from .core import _gloo_mod_ns_dict
from .core import _gloo_class_ns_dict
from .core import _gloo_func_ns_dict
from .core import _gloo_ctype_ns_dict

from .core import error, GLOOTypeError, GLOOValueError
from .core import _shim_doc, _gloo_func_doc, _gloo_func_desc_doc
from .core import _gloo_method_doc, _gloo_class_doc
from .core import _set_gloo_doc_namespace

from .extern import optional_package

#------------------------------------------------------------------------------

