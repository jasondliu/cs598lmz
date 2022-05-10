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
