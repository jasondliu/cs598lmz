import gc, weakref

class A(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name

class B(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'B(%s)' % self.name

a = A('a')
b = B('b')

print 'a:', a
print 'b:', b

# create a weak reference to a
a_ref = weakref.ref(a)
print 'a_ref:', a_ref

# create a weak reference to b
b_ref = weakref.ref(b)
print 'b_ref:', b_ref

# delete a
del a

# delete b
del b

print 'a_ref:', a_ref
print 'b_ref:', b_ref

# force garbage collection
gc.collect()

print 'a_ref:', a_ref
print '
