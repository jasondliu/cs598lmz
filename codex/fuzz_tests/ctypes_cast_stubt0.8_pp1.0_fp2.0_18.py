import ctypes
ctypes.cast(10, ctypes.py_object)

import ptypes
p = ptypes.pint.uint32_t()
p.set(10)
p.get()
p.cast(ctypes.py_object)

import ptypes, ctypes
p = ptypes.pint.uint32_t()
p.set(10)
p.cast(ctypes.py_object)
