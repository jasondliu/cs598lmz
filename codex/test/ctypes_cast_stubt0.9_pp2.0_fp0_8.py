import ctypes
ctypes.cast(0, ctypes.py_object)
ctypes.cast(0, ctypes.py_object) # again

import ctypes as _ctypes
_ctypes = _ctypes  # make sure we keep a reference
_ctypes.cast(0, _ctypes.py_object)
_ctypes.cast(0, _ctypes.py_object) # again


import ctypes as cty
cty = cty  # make sure we keep a reference
cty.cast(0, cty.py_object)
cty.cast(0, cty.py_object) # again


def f():
    import ctypes
    ctypes.cast(0, ctypes.py_object)
    ctypes.cast(0, ctypes.py_object)
f()
f()


def g():
    import ctypes as _ctypes
    _ctypes = _ctypes  # make sure we keep a reference
    _ctypes.cast(0, _ctypes.py_object)
