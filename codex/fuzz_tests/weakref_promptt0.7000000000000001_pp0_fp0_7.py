import weakref
# Test weakref.ref() with a class instance.
import weakref

class C(object):

    def __init__(self, x):
        self.x = x


c = C(42)
r = weakref.ref(c)
print(r().x)

c = None
assert r() is None

print('ok')
