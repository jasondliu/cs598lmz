import gc, weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'Goodbye, %s' % self.name

def bar(obj):
    print 'Hello, %s' % obj.name

def main():
    f = Foo('Alex')
    bar(f)
    f = None
    print 'Before gc'
    gc.collect()
    print 'After gc'

if __name__ == '__main__':
    main()
