import gc, weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def main():
    foo = Foo('foo')
    print 'foo:', foo
    bar = Foo('bar')
    print 'bar:', bar
    print 'weakref(foo):', weakref.ref(foo)
    print 'weakref(bar):', weakref.ref(bar)
    print 'gc.collect():', gc.collect()
    print 'weakref(foo):', weakref.ref(foo)
    print 'weakref(bar):', weakref.ref(bar)

if __name__ == '__main__':
    main()
