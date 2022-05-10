fn = lambda: None
gi = (i for i in ())
fn.__code__ = object()
fn.__code__ = sys.maxsize + 1
fn.__code__ = gi
try:
    fn.__code__ = b'a'
except TypeError:
    pass
else:
    raise Exception("Expected TypeError")

# __code__ as non-function attribute
class A:
    pass
A.__code__ = object()
A.__code__ = sys.maxsize + 1
A.__code__ = 1

# __code__ as non-function attribute, with descriptor
class B:
    def __get__(self, obj, typ=None):
        pass
class C:
    __code__ = B()

# __code__ as function attribute
def fn():
    pass
fn.__code__ = object()
fn.__code__ = sys.maxsize + 1
fn.__code__ = 1

# __code__ as function attribute, with descriptor
class A:
    def __get__(self, obj, typ=None):
        pass
def fn():
    pass
fn.__code__ = A()

#
