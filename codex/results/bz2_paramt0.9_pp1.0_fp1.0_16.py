from bz2 import BZ2Decompressor
BZ2Decompressor.__doc__ = BZ2Decompressor.decompress.__doc__
from bz2 import BZ2File
import marshal

DEBUG = 1

#xload(str('modules/__init__'))

#from types import *
from types import MethodType
from types import BuiltinFunctionType
from types import BuiltinMethodType
from types import ModuleType
from types import FunctionType
from types import LambdaType
from types import UnboundMethodType
from types import _WrapperDescriptorType

class CodeType:
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        pass

# This, again, is not a good way but I do not want to export more
# functions from interpreter.c
#
# The variable names are the ones used in pyemu and should be changed together.
# They should reflect the variable names in the pyemu code.
#
# pyemu_emu_write and pyemu_emu_read are the script-side equivalents of
# the pyemu_emu_{
