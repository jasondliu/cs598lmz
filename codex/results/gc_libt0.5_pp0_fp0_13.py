import gc, weakref

class A(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print 'del', self.x

class B(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print 'del', self.x

# create an object with a cyclic reference
a = A(1)
b = B(2)
a.ref = b
b.ref = a

# create a weakref to the object
a_ref = weakref.ref(a)
b_ref = weakref.ref(b)

# delete the original reference to the object
del a
del b

# show that the weak reference is still alive
print a_ref(), b_ref()

# show that the weak reference can be used to access the object
print a_ref().x
print b_ref().x

# show that the object is still alive
print a_ref().ref.x
print b_ref().ref.x

# delete
