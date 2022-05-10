import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print('callback(', r, ')')

def test(obj):
    print('test(', obj, ')')
    p = weakref.proxy(obj)
    r = weakref.ref(obj, callback)
    print('p:', p)
    print('r:', r)
    print('p.name:', p.name)
    print('r().name:', r().name)
    print('p.name:', p.name)
    print('r().name:', r().name)
    print('p.name:', p.name)
    print('r().name:', r().name)
    print('p.name:', p.name)
    print('r().name:', r().name)
    print('p.name:', p.name)
    print('
