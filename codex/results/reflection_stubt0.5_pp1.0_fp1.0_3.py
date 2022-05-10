fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__ = 42
(fn.__code__ is gi)
fn.__code__ = gi
fn.__code__ is gi
fn.__code__ = 42
fn.__code__ is 42

# __code__ should be read only
def fn():
    pass
try:
    fn.__code__ = fn.__code__
except TypeError:
    pass
else:
    print("did not raise TypeError")

# __code__ should be writable for classes
class C:
    pass
C.__code__ = 42
C.__code__ is 42

# __code__ should be writable for class instances
c = C()
c.__code__ = 42
c.__code__ is 42

# __code__ should be writable for functions
def fn():
    pass
fn.__code__ = 42
fn.__code__ is 42

# __code__ should be writable for builtins
int.__code__ = 42
int.__code__ is 42

# __code__ should be writable for modules

