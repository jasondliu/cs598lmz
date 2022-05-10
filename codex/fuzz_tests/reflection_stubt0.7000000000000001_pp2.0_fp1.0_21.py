fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
pickle.dumps(fn)

# same but with a method
class C(object):
    def __init__(self):
        self.__class__.m = lambda self: None
        self.m.__func__.__code__ = gi.gi_code
c = C()
pickle.dumps(c.m)

# Trying to pickle reference to a module dictionary must raise a
# TypeError.
try:
    pickle.dumps(sys)
except TypeError:
    pass
else:
    raise RuntimeError

# Same for __main__.
try:
    pickle.dumps(__main__)
except TypeError:
    pass
else:
    raise RuntimeError

# Try to pickle a traceback.
try:
    raise Exception
except:
    pickle.dumps(sys.exc_info()[2])

# Try to pickle a frame.
def foo():
    pickle.dumps(foo.f_back)
foo()

# Test the state of the C
