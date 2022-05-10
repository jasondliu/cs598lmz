import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.c_char_p)]
    def __repr__(self): return "hi"
    def _get_name(self): return "hi"
    name = property(_get_name)

s = S(b"123", b"456")
print(str(s))
s = ctypes.cast(s, ctypes.py_object).value
print(s.a, s.b)
print(s)
print(s.name)

from sys import getrefcount as grc

for i in range(100000):
    s = S(b"123", b"456")

print(grc(s))

#import gc
#gc.collect()

#import time
#time.sleep(1)
