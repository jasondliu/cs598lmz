fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18077: test that the __code__ attribute of a built-in function
# is not writable.
def f():
    pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in function is writable")

# Issue #18077: test that the __code__ attribute of a built-in method
# is not writable.
class C:
    def f(self):
        pass
try:
    C.f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in method is writable")

# Issue #18077: test that the __code__ attribute of a built-in method
# is not writable.
class C:
    def f(self):
        pass
try:
    C().f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in method is writ
