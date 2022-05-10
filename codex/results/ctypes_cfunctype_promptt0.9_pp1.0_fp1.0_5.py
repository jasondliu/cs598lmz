import ctypes
# Test ctypes.CFUNCTYPE(V)(KeepFirst(3)(func)) # OK

# OK:
from ctypes import *
@KeepFirst(3)(func)
</code>
The <code>ffi</code> will be built in place, but you could also use <code>ctypes.CDLL</code> or <code>ctypes.WinDLL</code> (or whatever <code>ctypes</code> DLL class you need).

