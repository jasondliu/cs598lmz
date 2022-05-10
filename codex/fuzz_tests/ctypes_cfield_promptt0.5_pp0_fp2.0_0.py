import ctypes
# Test ctypes.CField.from_param
class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char),
                ('b', ctypes.c_short),
                ('c', ctypes.c_int),
                ('d', ctypes.c_long),
                ('e', ctypes.c_longlong),
                ('f', ctypes.c_float),
                ('g', ctypes.c_double),
                ('h', ctypes.c_char_p)]

c = C()

c.a = 'a'
c.b = 2
c.c = 3
c.d = 4
c.e = 5
c.f = 6.6
c.g = 7.7
c.h = "hello"

c_from_param = ctypes.CField.from_param

c_from_param(c.a)
c_from_param(c.b)
c_from_param(c.c)
c_from_param(c.d)
c_from_param(c.e)
c
