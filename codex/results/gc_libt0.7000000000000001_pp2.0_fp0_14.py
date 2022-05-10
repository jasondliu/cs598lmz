import gc, weakref
from collections import defaultdict
from .util import parse_args, parse_kwargs
from .log import log_raise
from . import objtypes
from .objtypes import Type
from .objtypes import *
from .valuetypes import ValueType
from .valuetypes import *
from .objutils import *
from .objutils import _wrap_method
from .objutils import _wrap_method_with_args
from .objutils import _wrap_method_with_args_and_kwargs

import llvm.core
import llvm.passes
import llvm.ee

from llvm.core import LLVMException

from ctypes import CDLL, RTLD_GLOBAL

# ------------------------------------------------------------------------
# Low-level wrappers of LLVM objects
# ------------------------------------------------------------------------

def wrap_value(ll_value):
    """
    Wrap an LLVM value with a higher-level object.

    * `ll_value` is an LLVM value
    """
    if not ll_value:
        return None
    else:
        return ll_value._wrapping_obj


