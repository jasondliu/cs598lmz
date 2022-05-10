import ctypes
# Test ctypes.CFUNCTYPE
#
# Note: In the C code below, we use the "__attribute__((stdcall))" calling
# convention to ensure that we test that as well.

import ctypes
from ctypes import *

if os.name == "nt":
    c_add = CFUNCTYPE(c_int, c_int, c_int)(("add", cdll), ((1, "a"), (1, "b")))
    assert c_add(1, 1) == 2
    assert c_add(2, 3) == 5

    c_add2 = CFUNCTYPE(c_int, c_int, c_int)(("add", cdll), ((1, "a"), (1, "b")))
    assert c_add2(1, 1) == 2
    assert c_add2(2, 3) == 5

    c_add3 = CFUNCTYPE(c_int, c_int, c_int)(("add", cdll), ((1, "a"), (1, "b")))
    assert c_add3(1, 1)
