import weakref
# Test weakref.ref()

class C(object):
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return 'C(%r)' % self.a

def callback(r):
    print 'callback(', r, ')'

def test(a):
    print 'test(', a, ')'
    c = C(a)
    r = weakref.ref(c, callback)
    print 'ref', r
    print 'c:', c
    print 'r():', r()
    print 'deleting c'
    del c
    print 'r():', r()

test(1)
print
test('hello')
print
test([1, 2, 3])
print
test(C(5))
print
test(C(C(6)))


class MyObject(object):
    def __init__(self):
        self.x = 10
        self.y = 20
        self.z = 30

    def foo(self):
        pass

obj = MyObject()

r =
