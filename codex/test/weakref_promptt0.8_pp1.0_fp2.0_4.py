import weakref
# Test weakref.ref when class members are weak references.
import pickle
import copy


class X(object):
    pass

class C(object):
    x = X()
    y = 1
    z = x
    def __init__(self):
        self.attr = self.x


c = C()
w = weakref.ref(c)

c_copy = copy.copy(c)
c_copy_proper = copy.deepcopy(c)
s = pickle.dumps(c)
c_pickle = pickle.loads(s)

del c

print(w())
print(w().x)
print(w().__dict__)
print(w().__dict__['x'])
print(w().__dict__['z'])
print(w().attr)

print('\nCopy test:')
print(c_copy)
print(c_copy.x)
print(c_copy.__dict__)
print(c_copy.__dict__['x'])
print(c_copy.__dict__['z'])

