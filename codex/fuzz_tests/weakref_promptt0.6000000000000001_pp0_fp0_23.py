import weakref
# Test weakref.ref(f)()

def f():
    pass

wf = weakref.ref(f)()
print(wf is f)

# Test weakref.ref(b)()

b = b'123'

wb = weakref.ref(b)()
print(wb is b)


class C:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'C(%r)' % self.value


# Test weakref.ref(c)()

c = C(1)
wc = weakref.ref(c)()
print(wc is c)


# Test weakref.ref(u)()

u = u'123'
wu = weakref.ref(u)()
print(wu is u)


# Test weakref.ref(l)()

l = [1, 2]
wl = weakref.ref(l)()
print(wl is l)


# Test weakref.ref(d)()

d = {1: 1
