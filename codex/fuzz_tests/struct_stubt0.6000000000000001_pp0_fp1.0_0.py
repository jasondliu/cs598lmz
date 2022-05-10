from _struct import Struct
s = Struct.__new__(Struct)
s.size = 0
s.format = ''
s.format_char = (0, 0, 0)
s.unpack_from = s.pack_from = s.pack = s.unpack = lambda *args, **kwargs: (0,)

try:
    import ctypes
except ImportError:
    pass
else:
    s = ctypes.c_int64()
    s.value = 0
    s.value = ''
    s.value = (0, 0, 0)
    s.value = {'foo': 'bar'}
    s.value = [1, 2, 3]
    s.value = (x for x in range(5))
    s.value = 1.5

# Check for missing __qualname__ on inner classes
class A(object):
    class B(object):
        def __init__(self):
            pass

# Check for missing __qualname__ on inner functions
def funcA(x):
    def funcB():
        pass

# Check for missing __qualname__ on inner methods
class C(object
