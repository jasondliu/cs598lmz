import ctypes
ctypes.cast(obj, newtype)

# <codecell>

import ctypes
ctypes.pointer(obj)

# <codecell>

import ctypes
ctypes.POINTER(ctypes.c_int)(1)

# <codecell>

import ctypes
ctypes.pointer(ctypes.c_int(1))

# <codecell>

import ctypes
ctypes.pointer(ctypes.pointer(ctypes.c_int(1)))

# <codecell>

import ctypes
ctypes.c_int.from_address(0)

# <codecell>

import ctypes
ctypes.c_int.from_address(id(1))

# <codecell>

import ctypes
ctypes.c_int.from_address(id(2)).value

# <codecell>

import ctypes
ctypes.c_int.from_address(id(1)).value = 2

# <codecell>

import ctypes
def get_value(obj):
    return ctypes.c_int
