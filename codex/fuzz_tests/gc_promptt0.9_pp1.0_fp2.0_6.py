import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()

def callback(x):
    print('In callback:', x)

class ExpensiveObj(object):
    def __del__(self):
        print('Deleting:', self)
gc.collect()

obj = ExpensiveObj()
r = weakref.ref(obj, callback)
print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())

gc.collect()
gc.garbage.reverse()
gc.garbage.append(gc.garbage)
print('garbage:', gc.garbage)

# Test issubclass()
print(issubclass(str, object))
print(issubclass(str, (bytes, object)))
print(issubclass(str, (bytearray, object)))
print(issubclass(str, (str, object)))
print(issubclass(str, bytes))
print(issubclass(str, bytearray))
