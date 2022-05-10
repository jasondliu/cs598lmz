import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

from ctypes import *
from ctypes import util
import ctypes.macholib.dyld
name = util.find_library('libc.dylib')
name = str(name)
f = CDLL(name)
f.fun.argtypes = [ctypes.py_object]
f.fun.restype = ctypes.py_object
f.fun(fun)
</code>


A:

It is a bug in <code>ctypes.util.find_library</code>, which is a wrapper around <code>ctypes.macholib.dyld.framework_find</code>.
<code>ctypes.macholib.dyld.framework_find</code> is looking for the framework name in the usual places: <code>os.environ['DYLD_FRAMEWORK_PATH']</code>, <code>os.environ['DYLD_FALLBACK_FRAMEWORK_PATH']</code>, <code>os.environ['HOME']/Library/Frameworks</code>, <code>/Library/Frameworks
