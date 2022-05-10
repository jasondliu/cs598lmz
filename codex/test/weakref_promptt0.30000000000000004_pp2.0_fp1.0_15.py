import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print('callback(', r, ')')

def test():
    f = Foo('f')
    r = weakref.ref(f, callback)
    p = weakref.proxy(f, callback)
    print('f:', f)
    print('r:', r)
    print('p:', p)
    print('r():', r())
    print('p.name:', p.name)
    print('deleting f')
    del f
    gc.collect()
    print('r():', r())
    print('p.name:', p.name)

test()
