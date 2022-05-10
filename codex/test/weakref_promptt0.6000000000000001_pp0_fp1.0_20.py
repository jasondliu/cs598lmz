import weakref
# Test weakref.ref

class C(object):
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(bool(r))
del o
print(r())
print(bool(r))

class D(object):
    def __init__(self, label):
        self.label = label
    def __repr__(self):
        return 'D(%s)' % self.label

o = D('o')
d = {o: 'content'}
r = weakref.ref(o)
print(r in d)
print(d[r])

# Test weakref.proxy

o = C()
p = weakref.proxy(o)
print(p)
print(p.__class__)
print(p.undefined_attribute)
del o
print(p.undefined_attribute)

o = D('o')
p = weakref.proxy(o)
print(p)
print(p.__class__)
print(p.label)
del o
