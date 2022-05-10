import gc, weakref

@WeakKeyDictionary
class Foo(object):
    """A class with a WeakKeyDictionary"""

f = Foo()
f.name = 'f'
d = {f: 'f'}

f2 = Foo()
f2.name = 'f2'
d[f2] = 'f2'

f3 = Foo()

del f2

print f.__dict__
print d

print '1', f.name
print '2', d[f]

del f

print '3', len(d)

print repr(d)

#print gc.get_referrers(f)
#print gc.get_referrers(f2)

print gc.collect()
