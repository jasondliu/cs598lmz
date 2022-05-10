import ctypes
# Test ctypes.CFUNCTYPE(), ctypes.pointer() and ctypes.cast()
#

from ctypes import *


##PYB11_begin_exceptions
class MyError(Exception):
    pass
##PYB11_end_exceptions

import sys

##PYB11_begin_preamble
from pyre.components.Component import Component
from pyre.applications.Script import Script

##PYB11_end_preamble

##PYB11_begin_wrapping_pyre_namespace
##PYB11_end_wrapping_pyre_namespace

##PYB11_begin_declarations
##PYB11_end_declarations

class dll_test(Script):

    ##PYB11_begin_class(dll_test)
    ##PYB11_end_class(dll_test)

    def main(self, *args, **kwds):
        # CFUNCTYPE instances must always be used as callback type specifiers.
        # You can use a CFUNCTYPE instance as the
