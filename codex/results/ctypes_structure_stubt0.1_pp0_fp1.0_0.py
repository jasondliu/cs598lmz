import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.Structure is a subclass of ctypes.Union, which is a subclass of ctypes.BigEndianStructure, which is a subclass of ctypes.LittleEndianStructure, which is a subclass of ctypes.Array, which is a subclass of ctypes.POINTER, which is a subclass of ctypes.CDLL, which is a subclass of ctypes.PyDLL, which is a subclass of ctypes.WinDLL, which is a subclass of ctypes.LibraryLoader, which is a subclass of ctypes.util.find_library, which is a subclass of ctypes.util.find_msvcrt, which is a subclass of ctypes.util.find_library, which is a subclass of ctypes.util.find_library, which is a subclass of ctypes.util.find_library, which is a subclass of ctypes.util.find_library, which is a subclass of ctypes.util.
