import weakref
# Test weakref.ref() over a weakref.WeakSet() of deque items

class A(object):
    pass

as = weakref.WeakSet()
for i in range(21):
    a = A()
    as.add(a)
    w = weakref.ref(a)
    a = None
print(len(as))

class B(object):
    def __del__(self):
        raise Exception

bs = weakref.WeakSet()
for i in range(21):
    b = B()
    bs.add(b)
    w = weakref.ref(b)
    b = None
print(len(bs))

class C(object):
    def __del__(self):
        raise Exception
    def __hash__(self):
        return id(self)

cs = weakref.WeakSet()
for i in range(21):
    c = C()
    cs.add(c)
    w = weakref.ref(c)
    c = None
print(len(cs))

# Test weakref.ref() over
