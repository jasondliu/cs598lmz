import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def _as_parameter_ (self):
    return self
ctypes.c_int.from_param = _as_parameter_

class C:
    def __init__(self):
        self._as_parameter_ = self

c = C()

f = FUNTYPE(lambda x: x)
f(c)
</code>

