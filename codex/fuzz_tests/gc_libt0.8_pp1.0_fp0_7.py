import gc, weakref

def callback(reference):
    print('collected', reference)

obj = MyClass()
r = weakref.ref(obj, callback)
print('obj', obj)
print('ref', r)
print('r()', r())
print()

del obj
gc.collect()
print('obj', obj)
print('ref', r)
print('r()', r())
print()


obj = MyClass()
r = weakref.ref(obj)

def bye():
    print('Gone with the wind...')

ender = weakref.finalize(obj, bye)
print(ender.alive)

del obj
print(ender.alive)

gc.collect()
print(ender.alive)
