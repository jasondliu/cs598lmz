import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect after a Python function returns
# will collect all unreachable objects, including those with finalizers
def baz():
    class Foo:
        def __del__(self):
            print 'Foo.__del__'
    f = Foo()
    print "Calling gc.collect"
    gc.collect()
baz()

# Test gc.collect after a Python function returns
# will collect all unreachable objects, including those with finalizers
def baz():
    class Foo:
        def __del__(self):
            print 'Foo.__del__'
    f = Foo()
    print "Calling gc.collect"
    gc.collect()
baz()


class A(object):

    def __del__(self):
        print 'A.__del__'

class B(A):
    def __del__(self):
        print 'B.__del__'
        super(B, self).__del__()

class C(object):

    def __del__(self):
        print 'C.__del__'

class D(
