import ctypes
# Test ctypes.CFUNCTYPE
# This file is part of the oocx compiler. 
# Copyright (c) Daniele Pallastrelli.
# See the LICENSE file for details.
#
# To test:
#     python test_CFUNCTYPE.py
#

#
# Basic case
#

def test_CFUNCTYPE_basic():
    # simple add
    @ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    def add(a, b):
        return a + b

    import operator

    assert type(add) is type(operator.add)
    assert add(2, 3) == add(item1=2, item2=3) == 5
    assert add(5, 7) == add(item1=5, item2=7) == 12

#
# Long argument list
#

N = 9
a = range(N)
b = range(1, N+1)
