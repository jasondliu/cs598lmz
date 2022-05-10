import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.Structure is a subclass of ctypes.Union
# ctypes.Union is a subclass of ctypes.BigEndianStructure
# ctypes.BigEndianStructure is a subclass of ctypes.LittleEndianStructure
# ctypes.LittleEndianStructure is a subclass of ctypes.Structure

# ctypes.Structure is a subclass of ctypes.Array
# ctypes.Array is a subclass of ctypes.BigEndianStructure
# ctypes.BigEndianStructure is a subclass of ctypes.LittleEndianStructure
# ctypes.LittleEndianStructure is a subclass of ctypes.Array

# ctypes.Structure is a subclass of ctypes.Union
# ctypes.Union is a subclass of ctypes.BigEndianStructure
# ctypes.BigEndianStructure is a subclass of ctypes.LittleEndianStructure
# ctypes
