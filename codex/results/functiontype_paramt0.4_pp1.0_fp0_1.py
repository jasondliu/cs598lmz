from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))

# __class__
class C: pass
foo = C()
foo.__class__

# __delattr__
class C:
    def __delattr__(self, name):
        print(name)
c = C()
del c.foo

# __dir__
class C: pass
dir(C)

# __doc__
class C:
    """docstring"""
C.__doc__

# __eq__
class C: pass
c1 = C()
c2 = C()
c1 == c2

# __format__
class C: pass
"{0:foo}".format(C())

# __ge__
class C: pass
c1 = C()
c2 = C()
c1 >= c2

# __getattribute__
class C:
    def __getattribute__(self, name):
        print(name)
c = C()
c.foo

# __gt__
class C: pass
c1 = C()
c2 = C()
c
