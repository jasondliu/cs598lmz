import weakref
# Test weakref.ref
class C:
    pass
c = C()
r = weakref.ref(c)
print 'c=', c
print 'r=', r
print 'r()=', r()
c2 = r()
print 'c is c2:', c is c2
del c
print 'del c'
print 'r()=', r()
print 'r() is None:', r() is None
print 'r() is None:', r() is None
print 'c2=', c2

# Test weakref.proxy
p = weakref.proxy(c2)
print 'p=', p
print 'p.__class__=', p.__class__
print 'p.__class__.__name__=', p.__class__.__name__
print 'type(p)=', type(p)
print 'type(p).__name__=', type(p).__name__
print 'p.a=1'
try:
    p.a = 1
except ReferenceError, e:
    print 'ReferenceError:', e
print 'del c2'

