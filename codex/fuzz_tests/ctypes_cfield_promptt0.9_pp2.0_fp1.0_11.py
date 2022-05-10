import ctypes
# Test ctypes.CField = ctypes.POINTER(ctypes.CFUNCTYPE())
#
# The code below is being translated by cython to:
#    # Field type is 'CFUNCTYPE(* CFUNCTYPE())'
#    self.pt = <CFUNCTYPE * CFUNCTYPE()>((<CFUNCTYPE * CFUNCTYPE()>(pdata))[0])
#
# gcc 4.7.2 complains about this code:
#
# test_ctypes.c: In function ‘__pyx_f_5test_1ctypes_pt_set’:
# test_ctypes.c:2025:44: error: subscripted value is neither array nor pointer
#       # Field type is 'CFUNCTYPE(* CFUNCTYPE())'
#                                       ^
#
# Other versions of gcc probably have this issue too.

from ctypes import *


class Test(object):

    def __init__(self):
        self._pt = None

    def pt_get(self):
        return self._pt

    def
