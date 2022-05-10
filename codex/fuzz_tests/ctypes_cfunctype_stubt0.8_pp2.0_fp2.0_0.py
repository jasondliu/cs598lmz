import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return MyTest(1)

print fun()
</code>
output:
<code>&lt;__main__.MyTest object at 0x00000000022EE320&gt;
</code>
I don't understand why I need to use <code>ctypes</code> here. My question is how can I do this without using <code>ctypes</code> (I know it's possible, because I've seen Pybind11 doing this). I have to mention that it's important for me to use <code>@cfunc</code> decorator (actually I really need to use it in more complicated scenarios, that's why I need to understand how it works).


A:

You can write own decorator with required functionality:
<code>from ctypes    import CFUNCTYPE, c_char_p
from ctypes    import c_int, c_bool, c_double
from ctypes    import c_void_p, py_object, cast
from ctypes    import pythonapi
from collections import namedtuple
from inspect   import getargspec
from functools import wraps
import sys


