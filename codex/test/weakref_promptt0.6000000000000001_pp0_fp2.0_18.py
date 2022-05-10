import weakref
# Test weakref.ref for the given object.
# The object should have no __del__ method.
# If the __del__ method prints a message, the test will fail.
# If create() returns None, the test passes.
# Otherwise, the test fails, and create() should print an error message.

def check_basic(obj):
    a = weakref.ref(obj)
    b = weakref.ref(obj)
    c = weakref.ref(obj)
    #print 'obj:', obj
    #print 'a:', a
    #print 'b:', b
    #print 'c:', c
