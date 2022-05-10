import weakref
# Test weakref.ref()

class A:
    pass

a = A()
wr = weakref.ref(a)
print(wr)
print(wr())

del a
print(wr)
print(wr())

# Test weakref.proxy()

class B:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "B(%s)" % self.value

b = B(10)
wp = weakref.proxy(b)
print(wp)
print(wp.value)

del b
print(wp)
print(wp.value)
