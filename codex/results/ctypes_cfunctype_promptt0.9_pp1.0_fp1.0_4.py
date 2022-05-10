import ctypes
# Test ctypes.CFUNCTYPE()
from ctypes import *
from ctypes import util
PYLIB = util.find_library("python")
LIBC = CDLL(PYLIB)
from _ctypes import FUNCFLAG_CDECL
from ctypes import _CFuncPtr
from ctypes import cast, POINTER
#


from ctypes import *
import platform
from mypython.clibs import ifc
from  mypython.cstructs import *

from  mypython.cstdiobind import *



MELANGE_RELEASE_DATE = "August 21, 2019"
MELANGE_VERSION_NUMBER = "1.06"
# All at interface functions:
#ifc.parmu.restype = c.c_void_p

#-------------------------------------------------------

def MY_REPR(mystring):
    import cgi
    return cgi.escape(mystring)


def MY_LIST(mylist):
    retlist = []
    for item in mylist:
        retlist.append(MY_REPR(item))
    return "[" + ", ".
