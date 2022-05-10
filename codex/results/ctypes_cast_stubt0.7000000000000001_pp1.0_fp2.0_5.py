import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a new old-style class.
class X(object): pass
x = X()

# Create a new memory block.
addr = id(x) & ~0xFFF

# Make the block writable.
ctypes.pythonapi.mprotect(addr, 0x1000, 0x04 | 0x02)

# This will crash the interpreter.
ctypes.cast(id(x), ctypes.POINTER(ctypes.c_char))[16] = '\0'
