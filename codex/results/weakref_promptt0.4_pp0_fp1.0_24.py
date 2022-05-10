import weakref
# Test weakref.ref() constructor for non-callable objects.
class C:
    pass

for obj in [None, 1, 'a', 1.2, [], (), {}]:
    try:
        ref = weakref.ref(obj)
    except TypeError:
        pass
    else:
        raise RuntimeError, "expected TypeError"

# Test weakref.ref() constructor for callable objects.
class C:
    def __call__(self, *args):
        return args

for obj in [C(), lambda: None, weakref.ref]:
    ref = weakref.ref(obj)
    if ref() is not obj:
        raise RuntimeError, "ref() returned wrong object"

# Test weakref.ref() constructor for objects with a __call__ method
# that raises an exception.
class C:
    def __call__(self):
        raise RuntimeError

obj = C()
ref = weakref.ref(obj)
try:
    ref()
except RuntimeError:
    pass
else:
    raise RuntimeError, "expected RuntimeError"

# Test weak
