import weakref
# Test weakref.ref() on a function.
import weakref

class Wrapper:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        return self.func(*args)

def f(x):
    return x

w = Wrapper(f)
r = weakref.ref(w)
w = None

assert r()()(3) == 3

# Test weakref.ref() on a method
import weakref

class C:
    def f(self, x):
        return x

c = C()
r = weakref.ref(c.f)
c = None

assert r()(3) == 3

# Test weakref.ref() on a builtin
import weakref

r = weakref.ref(len)

assert r()([1,2,3]) == 3

# Test weakref.ref() on a builtin method
import weakref

class C:
    def __len__(self):
        return 3

c = C()
r = weakref.
