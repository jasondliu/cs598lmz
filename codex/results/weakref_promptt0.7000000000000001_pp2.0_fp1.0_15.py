import weakref
# Test weakref.ref() and weakref.proxy().

class A(object):
    def __init__(self):
        self.a = 1
    def __str__(self):
        return "A()"

# Test weakref.ref(obj)

print('ref')
a = A()
r = weakref.ref(a)
print(r())
del a
try:
    print(r())
except Exception as e:
    print(e)

# Test weakref.ref(obj, callback)

print('ref callback')
def cb(r):
    print('callback')
a = A()
r = weakref.ref(a, cb)
del a
print('callback not called')

# Test weakref.proxy(obj)

print('proxy')
a = A()
p = weakref.proxy(a)
print(p)
del a
try:
    print(p)
except Exception as e:
    print(e)

# Test weakref.ref(obj) with a non-weakable type

print('ref nonweak')
