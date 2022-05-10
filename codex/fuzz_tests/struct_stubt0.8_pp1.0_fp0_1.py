from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
s.format = Struct.format
s

from ctypes import *
def print_int(n):
    print(n)

callable_ = c_int.__call__
callable_.argtypes = (c_int,)
callable_.restype = None
callable_.errcheck = None
callable_.__name__ = 'print_int'

from functools import partial
print_int = partial(print_int, None)
print_int


from collections import OrderedDict
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
''.join(d.keys())

d.move_to_end('b', last=False)
''.join(d.keys())


from collections import UserDict
class MyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return
