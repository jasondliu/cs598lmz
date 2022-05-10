import weakref
# Test weakref.ref()

def callback(reference):
    print('callback(', reference, ')')

ob = weakref.ref(object(), callback)
print('ob:', ob)

print('deleting ob')
del ob

print('deleting object')
