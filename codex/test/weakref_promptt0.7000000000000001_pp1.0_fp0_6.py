import weakref
# Test weakref.ref()

class foo(object):    
    pass

x = foo()
y = foo()

# Create a weakref to y
a = weakref.ref(y)

# Create a weakref to x, but with a callback
def callback(object):
    print(object)
w = weakref.ref(x, callback)

del y
del x

print(a())
print(w())

print('end')
