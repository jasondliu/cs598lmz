import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(arg):
    print 'my_callback(%d)' % arg
    return arg

my_callback_c = FUNTYPE(my_callback)

from ctypes import *

lib = cdll.LoadLibrary('./libtest.so')

lib.set_callback(my_callback_c)

lib.test()
</code>
Output:
<code>my_callback(1)
</code>

