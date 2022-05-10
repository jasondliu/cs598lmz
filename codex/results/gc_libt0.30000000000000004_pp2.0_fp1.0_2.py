import gc, weakref

class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass({!r})'.format(self.name)

gc.set_debug(gc.DEBUG_SAVEALL)

o = MyClass('instance to control')
wr = weakref.ref(o)

print('created:', wr)
print('created:', wr())

print('before, num_objects:', gc.get_count())

gc.collect()

print('after, num_objects:', gc.get_count())

print('unreachable:', gc.garbage)

print('deleting o')
del o
print('unreachable:', gc.garbage)

print('still alive:', wr())

print('deleting wr')
del wr
print('unreachable:', gc.garbage)
