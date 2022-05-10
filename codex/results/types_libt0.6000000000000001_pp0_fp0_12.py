import types
types.new_class( "C", (object,) )

class D(object):
    pass

c = C()
d = D()

print c.__class__
print d.__class__

c.__class__ = D

print c.__class__
print d.__class__

print C.__class__
print D.__class__

C.__class__ = D

print C.__class__
print D.__class__

print type(c)
print type(d)

print type(C)
print type(D)

print C.__class__.__class__
print D.__class__.__class__

C.__class__.__class__ = D

print C.__class__.__class__
print D.__class__.__class__

print type(C)
print type(D)

print C.__class__.__class__
print D.__class__.__class__

print type(C.__class__)
print type(D.__class__)
