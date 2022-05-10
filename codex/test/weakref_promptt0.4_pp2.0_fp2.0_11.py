import weakref
# Test weakref.ref() on a non-weakrefable object.
class C:
    pass

c = C()

try:
    weakref.ref(c)
except TypeError as err:
    print(err)
    print('ok')
else:
    print('not ok')
# Test weakref.ref() on a weakrefable object.
class C:
    pass

c = C()

try:
    weakref.ref(c)
except TypeError as err:
    print('not ok')
    print(err)
else:
    print('ok')
# Test weakref.ref() on a weakrefable object.
class C:
    pass

c = C()

try:
    weakref.ref(c)
except TypeError as err:
    print('not ok')
    print(err)
else:
    print('ok')
# Test weakref.ref() on a weakrefable object.
class C:
    pass

c = C()

