import weakref
# Test weakref.ref

class MyClass:
    def __init__(self):
        self.my_attribute = 1

def callback(ref):
    print('callback', ref)

obj = MyClass()
ref = weakref.ref(obj, callback)

print(ref)
print(ref())
print(obj)
print(obj.my_attribute)
print('****')
obj = None
ref()
print('****')
print(ref())

# Test weakref.finalize
class MyClass:
    def __init__(self):
        self.my_attribute = 1

def callback(ref):
    print('callback', ref)

obj = MyClass()
ref = weakref.finalize(obj, callback)

print(ref)
print(obj)
print('****')
obj = None
ref()
