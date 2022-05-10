import weakref
# Test weakref.ref()
def callback(obj):
    print('callback', obj)

def callback2(obj):
    print('callback2', obj)

obj = object()
ref = weakref.ref(obj, callback)
ref2 = weakref.ref(obj, callback2)
print('obj:', obj, 'ref:', ref, 'ref2:', ref2)

print('del obj')
del obj
print('ref:', ref, 'ref2:', ref2)

print('del ref')
del ref
print('ref:', ref, 'ref2:', ref2)

print('del ref2')
del ref2
print('ref:', ref, 'ref2:', ref2)

# Test weakref.WeakKeyDictionary()
class Object(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

d = weakref.WeakKeyDictionary()
o1 = Object('o1')
o2 = Object('o2')
print('d:', d)
