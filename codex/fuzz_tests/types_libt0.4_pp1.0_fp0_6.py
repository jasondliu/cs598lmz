import types
types.MethodType(f, None, A)

# This is an error in Python 2, but not in Python 3.
# The reason is that in Python 2, methods were not first-class objects,
# so you could not pass them around like this.
# In Python 3, methods are first-class objects, so you can pass them around.
# This is a very useful feature, but it does mean that you have to be careful
# not to pass around methods that depend on the object that they are bound to.
# In this case, the method f depends on self, which is bound to A.
# If you pass the method to another object, then it is no longer bound to A,
# so it will not work.
# You can see this if you try to call the method:

try:
    B = A()
    B.f()
except:
    logging.exception('Expected')
else:
    assert False

# This is an error because B is not an instance of A.
# If you want to pass around methods, you have to be careful to make sure
# that they are bound to the right object.
