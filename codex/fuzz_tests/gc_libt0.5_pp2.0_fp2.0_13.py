import gc, weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

gc.set_debug(gc.DEBUG_LEAK)
a = Foo('a')
w = weakref.ref(a)

print('a:', a)
print('w:', w)
print('w():', w())
print('deleting a')
del a
gc.collect()
print('w():', w())
