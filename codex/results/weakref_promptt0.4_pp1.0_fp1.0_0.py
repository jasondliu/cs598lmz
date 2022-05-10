import weakref
# Test weakref.ref(x) for all types.

import weakref

def test(x):
    print(type(x), end=' ')
    r = weakref.ref(x)
    print(r, end=' ')
    print(r())

test(None)
test(1)
test(1.1)
test(1+2j)
test(b'abc')
test(u'abc')
test('abc')
test(object())
test(object)
test(test)

# Test weakref.ref(x) for cyclic types.

import weakref

def test(x):
    print(type(x), end=' ')
    r = weakref.ref(x)
    print(r, end=' ')
    print(r())

class C:
    pass

c = C()
c.c = c
test(c)

l = []
l.append(l)
test(l)

t = ()
t += (t,)
test(t)

d = {}
d[0] = d
