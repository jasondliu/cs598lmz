import gc, weakref

class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass({!r})'.format(self.name)

o = MyClass('instance')
r = weakref.ref(o)
print(r)
print(r())
print(o)
print(r() is o)
print(r() is None)

o = None
gc.collect()
print(r() is None)

print('\n')

class ExpensiveObject:
    def __del__(self):
        print('(Deleting {})'.format(self))

def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))

obj = ExpensiveObject()
r = weakref.ref(obj, callback)
print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())


