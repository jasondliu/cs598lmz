import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_long
    z = 'y'
    _fields_ = [('x', ctypes.c_char),
                ('y', ctypes.c_long),
                ('z', 'y'),
               ]

#    x = ctypes.c_char
#    x = 'x'
#    def __init__(self, x):
#        self.x = x

# http://stackoverflow.com/questions/37152932/what-are-all-the-c-typedefs-available-in-ctypes
# https://docs.python.org/3/library/ctypes.html#ctypes.Structure

with open('/dev/urandom', 'rb') as fd:
    s = S.from_buffer(fd)
    print(s)
    print()
    for v in s._fields_:
        print(v)
