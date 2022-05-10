import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

# ctypes.Structure is a subclass of ctypes.Union.
# ctypes.Union is a subclass of ctypes.BigEndianStructure.
# ctypes.BigEndianStructure is a subclass of ctypes.LittleEndianStructure.
# ctypes.LittleEndianStructure is a subclass of ctypes.StructBase.
# ctypes.StructBase is a subclass of ctypes.Array.
# ctypes.Array is a subclass of ctypes.CDLL.
# ctypes.CDLL is a subclass of ctypes.PyDLL.
# ctypes.PyDLL is a subclass of ctypes.WinDLL.
# ctypes.WinDLL is a subclass of ctypes.LibraryLoader.
# ctypes.LibraryLoader is a subclass of ctypes.PyCArgObject.
# ctypes.PyCArgObject is a subclass of ctypes.PyCData.

