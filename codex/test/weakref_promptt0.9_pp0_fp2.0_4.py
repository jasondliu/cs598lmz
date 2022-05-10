import weakref
# Test weakref.ref:

# Create a simple object:

class C(object):
    pass

obj = C()
obj.x = 10

# Create a weakref with a callable:

r1 = weakref.ref(obj, lambda x: obj == None)
