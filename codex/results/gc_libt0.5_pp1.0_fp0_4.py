import gc, weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'Goodbye, %s' % self.name

class Bar(Foo):
    def __init__(self, name):
        super(Bar, self).__init__(name)
        self.wr = weakref.ref(self)

def main():
    b = Bar('b')
    print b.wr()
    del b
    gc.collect()

if __name__ == '__main__':
    main()
</code>
I'm not sure if this is the best way to do this, but it seems to work.

