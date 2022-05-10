import gc, weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def foo():
    print 'in foo()'
    a = Foo('a')
    print 'a:', a
    b = Foo('b')
    print 'b:', b
    c = Foo('c')
    print 'c:', c
    wr = weakref.ref(a)
    print 'wr:', wr
    print 'wr():', wr()
    print 'a:', a
    print 'b:', b
    print 'c:', c
    del a
    print 'del a'
    print 'wr():', wr()
    print 'b:', b
    print 'c:', c
    del b, c
    print 'del b, c'
    print 'wr():', wr()
    gc.collect()
    print 'gc.collect()'
    print 'wr():', wr()

if __name__ == '
