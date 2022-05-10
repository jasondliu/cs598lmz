import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

def callback(wr):
    print('callback(', wr, ')')

def f():
    print('creating a list')
    x = []
    print('appending some items')
    for i in range(5):
        x.append(i)
    print('creating a ref to the list')
    r = weakref.ref(x, callback)
    print('returning from f()')
    return r

print('calling f()')
r = f()
print('calling gc.collect()')
gc.collect()
print('calling gc.collect() again')
gc.collect()
print('done')

# Test reference counting with a weakref callback

class A:
    pass

def callback(wr):
    print('callback(', wr, ')')

def f():
    print('creating an instance')
    x = A()
    print('creating a ref to the instance')
    r = weakref.ref(x, callback)
    print('returning from f()')
    return r
