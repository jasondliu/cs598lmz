import ctypes
ctypes.cast(0, ctypes.py_object).value

import numpy as np
x = np.arange(4)
print(x.ctypes.data)

import sys
print(sys.getsizeof(5))
print(sys.getsizeof(b'a'))
print(sys.getsizeof(bytearray(b'a')))
print(sys.getsizeof(u'a'))
print(sys.getsizeof(memoryview(b'a')))
print(sys.getsizeof(np.array(True)))

#--------
# ref-counting
x = 42
print(sys.getrefcount(x))
y = x
print(sys.getrefcount(x))
del x
print(sys.getrefcount(y))


#------
# cyclic ref-counting
a = {1,2}
b = {3,4}
a.add(b)
b.add(a)

#----
# weak references
import weakref
a = dict(one=1,two=2)
wref
