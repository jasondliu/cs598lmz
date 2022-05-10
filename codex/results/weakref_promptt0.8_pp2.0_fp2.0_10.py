import weakref
# Test weakref.ref on memoryview objects.

import weakref


a = memoryview(b'abc')
r = weakref.ref(a)
del a
try:
    a
except NameError:
    pass
else:
    raise Exception('NameError should be raised')
a = r()
b = memoryview(b'def')
try:
    b = r()
except TypeError:
    print('TypeError should be raised')
else:
    raise Exception('TypeError should be raised')
b = memoryview(b'def')
c = memoryview(b'ghi')
d = weakref.ref(c)
b = c
d() is c
