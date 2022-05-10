import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"
@FUNTYPE
def newfun(x):
    return x + " World"
fun()

newfun('Hello')

#import ctypes
#On 32-bit python, this line below works, but on 64-bit it doesn't
#import ctypes _winapi
#On 64-bit python, this line below works, it imports the old winapi.
#from ctypes import *
#from ctypes import _winapi


#On 32-bit python, this line below works, but on 64-bit it doesn't
#import ctypes _winapi
from ctypes import _winapi

from ctypes import *
from ctypes import _winapi


from ctypes import _winapi

import ctypes.util
from ctypes import *
from ctypes import _winapi
from ctypes import util

from ctypes import util
from ctypes import _winapi
import ctypes
import ctypes.util

from ctypes import util
from ctypes import _winapi
import ctypes
from ctypes import util

from ctypes import util
import ctypes
