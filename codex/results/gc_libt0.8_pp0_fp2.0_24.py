import gc, weakref, pickle

class Demo(object):
    pass

def weakref_callback(ref):
    print('callback: ref=%r' % ref)

ref = weakref.ref(Demo(), weakref_callback)
d = ref()
print('after: d=%r, ref()=%r' % (d, ref()))

d = None
print('after: d=%r, ref()=%r' % (d, ref()))

del ref
print('after: d=%r, ref()=%r' % (d, ref()))

gc.collect()
print('after: d=%r, ref()=%r' % (d, ref()))

class Vector(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __del__(self):
        print('Vector.__del__:', self)


