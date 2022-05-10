import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    def __del__(self):
        print ("A.__del__")

a = A()
print (a)
print (type(a))
print (dir(a))
print (type(A))
print (type(A.__del__))
print (type(A.__del__.__get__(a)))
print (type(A.__del__.__get__(None, A)))
print (type(A.__del__.__get__(None, A)(a)))
#del a
#print (a)
#print (type(a))
#print (dir(a))

# Test __del__()
#a.__del__()

# Test gc.collect()
#gc.collect()

# Test weakref
#a = A()
#b = weakref.ref(a)
#print (b)
#print (type(b))
#print (dir(b))
#print (b.__get__(a))
#print (b.__get__(None
