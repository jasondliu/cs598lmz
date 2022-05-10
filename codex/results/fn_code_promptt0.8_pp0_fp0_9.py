fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn.func_name
fn.func_name
# Test fn.__name__
fn.__name__


class C(object):

    def __init__(self):
        self.__x = 9

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    x = property(get_x, set_x)

    def meth(self):
        return self.x


# Test property type
C.x

# Test property access
C().meth()

# Test bound method
C().meth

# Test naked class
C

# Test with
with C() as c:
    c.x

# Test nested with
with C() as c1, C() as c2:
    c1.x
    c2.x

# Test with lambda
with lambda: None as _:
    pass

# Test with listcomps
with [i for i in range(1)]:
    pass

# Test with
