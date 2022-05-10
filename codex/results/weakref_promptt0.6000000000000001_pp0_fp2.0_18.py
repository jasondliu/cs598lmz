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
    if a() is not obj:
        print 'a() is not obj'
    if b() is not obj:
        print 'b() is not obj'
    if c() is not obj:
        print 'c() is not obj'
    if a is not b:
        print 'a is not b'
    if a is not c:
        print 'a is not c'
    if b is not c:
        print 'b is not c'
    if a() is
