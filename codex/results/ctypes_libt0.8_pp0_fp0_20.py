import ctypes
ctypes.cdll.LoadLibrary("./libfoo.so")
from libfoo import Foo
f = Foo()
f.foo.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
f.foo.restype = None
a = (ctypes.c_int*2)(*range(0, 2))
b = (ctypes.c_int*2)(*range(2, 4))
f.foo(a, b)
a, b

from libfoo import Foo
f = Foo()
f.foo.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
f.foo.restype = None
a = np.arange(2)
b = np.arange(2)
f.foo(a.ctypes.data_as(ctypes.POINTER(ctypes.c_int)), b.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
a, b

import ctypes
