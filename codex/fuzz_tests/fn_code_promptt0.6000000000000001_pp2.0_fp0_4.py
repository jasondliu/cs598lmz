fn = lambda: None
# Test fn.__code__

class A:
    def __init__(self):
        self.__class__ = B
        self.__init__()

class B:
    def __init__(self):
        self.__class__ = C
        self.__init__()

class C:
    def __init__(self):
        pass

a = A()
b = B()
c = C()

d = D()
e = E()
f = F()

# Test fn.__call__

g = G()
h = H()
i = I()

# Test fn.__getattr__

j = J()

# Test fn.__setattr__

k = K()

# Test fn.__delattr__

l = L()

# Test fn.__getattribute__

m = M()

# Test fn.__del__

n = N()

# Test fn.__cmp__

o = O()

# Test fn.__hash__

p = P()

# Test fn.__repr__
