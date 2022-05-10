import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32

s = S.from_address(0x80000000)
s.x = 1  # Causes segfault on 32 bit
s.y = 2  # Causes segfault on 32 bit
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
</code>
The behaviour is the same on Python 3.2.2 and 3.3.0. It may be a bug in ctypes but I don't know much about the internals of Python and ctypes.
I have tried to find information on this but hasn't found any so far.
I also did a program in C (Linux) and did the same thing.
