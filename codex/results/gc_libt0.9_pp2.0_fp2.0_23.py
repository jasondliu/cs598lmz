import gc, weakref
from struct import pack
from binascii import unhexlify
import array
from math import sqrt
from types import StringType, UnicodeType
import weakref

from parser import AttrExpressions, NoAttr, Network
from pyutilib.misc.container_iterator import DataRef

import pyomo.core.base.misc

import pyutilib.misc.tabular as tabular

#
# This function tests for the existence of a named function within
# the other modules in the Pyomo kernel.
#
def pysp_get_object(name):
    from pyomo.core import *

    try:
        mod = __import__(name)
        return getattr(mod, name)
    except:
        for other_name in __all__:
            if name.startswith(other_name):
                mod = __import__(other_name)
                return getattr(mod, name)
    raise (ImportError, "Unknown module/function "+name)

def pysp_format_object_name(object):
    return object()._gen_name
