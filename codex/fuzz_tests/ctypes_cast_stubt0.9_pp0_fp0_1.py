import ctypes
ctypes.cast(0xdeadbeaf, ctypes.c_void_p).value

a = int("deadbeaf", 16)
print a

b = int("0xdeadbeaf", 16)
print b

# FGB

ctypes.sizeof(ctypes.c_void_p)

# FGO

# can an int be used as memory address?
import ctypes
x = ctypes.c_int(0x12345678)
ctypes.cast(x, ctypes.c_void_p).value

ctypes.cast(hex(id(x)), ctypes.c_void_p).value

# FGP
print [x for x in dir(ctypes) if x.startswith("c_")]

import ctypes
ctypes.c_long(1).value # => 1
ctypes.c_long(1) + 1 == ctypes.c_long(2) # => True
ctypes.c_long(1) + ctypes.c_long(1) == ctypes.c_long(2) # => True


