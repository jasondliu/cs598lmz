import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    c = ctypes.c_char
    s = ctypes.c_short

class B(ctypes.BigEndianStructure):
    x = ctypes.c_short
    c = ctypes.c_char
    s = ctypes.c_short

class L(ctypes.LittleEndianStructure):
    x = ctypes.c_short
    c = ctypes.c_char
    s = ctypes.c_short

s = S()
b = B()
l = L()

s.x
"""
True
"""
s.c
"""
True
"""
s.s
"""
False
"""

b.x
"""
False
"""
b.c
"""
True
"""
b.s
"""
True
"""

l.x
"""
True
"""
l.c
"""
True
"""
l.s
"""
False
"""
