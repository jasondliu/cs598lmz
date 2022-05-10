import weakref
# Test weakref.ref(instance_method):
class Foo(object):
    def __init__(self, callback):
        self.callback = callback

    def __call__(self):
        print "Foo called with self: %s" % self
        self.callback()

def main():
    def bar():
        print "bar called"
    foo = Foo(bar)
    print "foo is: %s" % foo
    foo() # Prints "Foo called with self: <__main__.Foo object at 0x...>"
    foo.callback() # Prints "bar called"

    f = weakref.ref(foo)
    print "f: %s" % f()
    foo = None
    print "f: %s" % f()

if __name__ == '__main__':
    main()

"""
foo is: <__main__.Foo object at 0x104b3b3d0>
Foo called with self: <__main__.Foo object at 0x104b3b3d0>
bar called
f: <__main__.
