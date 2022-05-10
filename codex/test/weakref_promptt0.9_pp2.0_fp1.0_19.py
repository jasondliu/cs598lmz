import weakref
# Test weakref.ref

class A:
    p = 1
    def __init__(self):
        self.x = 10
        self.y = 'abcd'

a = A()
a.xx = 'hello'
a.yy = 'world'

b = weakref.ref(a)
print(b())
# get value: 1

c = weakref.ref(a.p)
print(c())
# get value: 1

d = weakref.ref(a.x)
print(d())
# get value: 10

e = weakref.ref(a.y)
print(e())
# get value: 'abcd'

f = weakref.ref(a.xx)
print(f())
# get value: 'hello'

g = weakref.ref(a.yy)
print(g())
# get value: 'world'

h = weakref.ref(b)
print(h())
# get value: <weakref at 0x7f114897f4c8; to 'weakref' at 0x7f11
