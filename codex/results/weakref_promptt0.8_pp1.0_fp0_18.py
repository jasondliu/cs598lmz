import weakref
# Test weakref.ref(x, callback)

class A:
    pass

def callback(x):
    print('callback({!r})'.format(x))

a = A()
a_id = id(a)
a_ref = weakref.ref(a, callback)

print('a:', a)
print('a_ref:', a_ref)
print('a_ref():', a_ref())
print('a is a_ref():', a is a_ref())

del a
print('a deleted')
print('a_ref():', a_ref())

a = A()
a_id = id(a)
a_ref = weakref.ref(a, callback)

print('a:', a)
print('a_ref:', a_ref)
print('a_ref():', a_ref())
print('a is a_ref():', a is a_ref())

a_ref_id = id(a_ref)
a_ref = None
print('a_ref deleted')
print('gc.collect()')

gc.collect()

