fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__ == gi

# Equivalence by inspection
def foo(x: 1 == 1, *y: (1,), z: 3):
    pass
sys.getframeinfo(foo.__code__)
inspect.getclosurevars(foo)
inspect.signature(foo)
# Equivalence by inheritance
class A(Thread): pass
class B(A): pass
issubclass(B, Thread)

# Equivalence by inheritance
class C(object, metaclass=type):
    def __eq__(self, other):
        return True
C() == 1

# Equivalence by inspection
b = bytes([1, 2, 3])[:2]
b == b'1\x02'

# Equivalence by inspection
def foo(x):
    return x
ftype = type(foo)
ftype.__code__ = lambda: None
foo(1)

class C(object):
    classmethod
    def foo(x):
        return x
c = C()
c.foo.__get
