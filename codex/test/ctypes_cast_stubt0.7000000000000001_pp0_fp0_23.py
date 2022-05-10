import ctypes
ctypes.cast(0x7fffffff, ctypes.c_void_p)

#<ctypes.c_void_p object at 0x7fffffff>

ctypes.cast(0x7fffffff, ctypes.c_char_p).value

#'\xff\xff\xff\x7f'

class POINTER(ctypes.c_void_p):
    pass

class counter(object):
    def __init__(self, i):
        self.i = i

    def incr(self):
        self.i += 1
        return self.i

#In [70]: c = counter(1)
#In [71]: c.incr()
#Out[71]: 2

#In [72]: c.incr()
#Out[72]: 3

counter_p = POINTER(counter)

#In [74]: ctypes.cast(0x7fffffff, counter_p).contents.incr()
#Out[74]: 4

#In [75]: ctypes.cast(0x7fffffff, counter_p).
