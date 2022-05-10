import gc, weakref

class C:
    def __init__(self, *args):
        self.args = args
    def __repr__(self):
        return 'C(*{!r})'.format(self.args)

obj = C(1, 2, 3)
r = weakref.ref(obj)
print(r)
print(r())
obj = None
print(r())

print('-'*60)

class ExpensiveObject:
    def __del__(self):
        print('(Deleting {})'.format(self))

def callback(reference):
    print('callback({!r})'.format(reference))

obj = ExpensiveObject()
r = weakref.ref(obj, callback)
print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())

print('-'*60)

class ExpensiveObject:
    def __del__(self):
        print('(Deleting {})'.format(self))
