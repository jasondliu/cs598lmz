import weakref
# Test weakref.ref() on a function
class C:
    pass
def f(): pass
r = weakref.ref(f)
r()
r = weakref.ref(C)
r().a = 1
