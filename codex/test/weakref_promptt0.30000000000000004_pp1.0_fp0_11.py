import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print('callback({!r})'.format(r))

def test_ref():
    f = Foo('normal')
    r = weakref.ref(f, callback)
    print('created weak reference {!r}'.format(r))
    print('callback called' if r() is None else 'callback not called')
    print('deleting f')
    del f
    print('callback called' if r() is None else 'callback not called')

def test_proxy():
    f = Foo('normal')
    p = weakref.proxy(f, callback)
    print('created weak proxy {!r}'.format(p))
    print('callback called' if p.name == 'normal' else 'callback not called')
    print('deleting f')
    del f
