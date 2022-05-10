from types import FunctionType
list(FunctionType(FunctionType.__code__, {}).__globals__.keys())

###
import types
list(types.FunctionType.__globals__)

###
import dis
dis.dis(types.FunctionType)

###
import types
types.FunctionType.__class__

###
import types
types.FunctionType.__class__.__mro__

###
import types
types.MethodType.__mro__

###
import types
types.FunctionType.__dict__

###
import types
types.FunctionType.__doc__

###
import sys
sys.getsizeof(types.FunctionType)

###
import sys
sys.getsizeof(FunctionType)

###
x = 1
import sys
sys.getsizeof(x)

###
x = 1
import sys
sys.getsizeof(x)

###
x = 1
import sys
sys.getsizeof(x)

###
x = 1
import sys
sys.getsizeof(x)

###
x = 1
import sys

