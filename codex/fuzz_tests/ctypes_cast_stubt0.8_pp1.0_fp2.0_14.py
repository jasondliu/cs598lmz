import ctypes
ctypes.cast(ctypes.cast(0, ctypes.POINTER(ctypes.c_int)), ctypes.c_void_p)

ctypes.cast(ctypes.cast(ctypes.cast(0, ctypes.POINTER(ctypes.c_int)), ctypes.c_void_p), ctypes.POINTER(ctypes.c_int))

p = ctypes.pointer(ctypes.c_int(1234))
p

p.contents

p1 = ctypes.cast(p, ctypes.POINTER(ctypes.c_char))
p1.contents

p1.contents = b'A'
p.contents

p2 = ctypes.cast(p1, ctypes.POINTER(ctypes.c_int))
p2.contents

p2.contents = 5678
p.contents

p2.contents = 1234

p[0]

p[1]

import ctypes
import binascii

class Color(ctypes.Structure):
    _fields_ =
