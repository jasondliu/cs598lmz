import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class to use as a test object
class C:
    pass

# Create an instance of C to be referenced
ob = C()

# Create a weak reference to ob, using ob as the callback
r = weakref.ref(ob, lambda x,y: None)

# Create a weak reference to ob, using a function as the callback
r2 = weakref.ref(ob, lambda x,y: None)

# Create a weak reference to ob, using a bound method as the callback
r3 = weakref.ref(ob, C().__del__)

# Create a weak reference to ob, using a bound method as the callback
# but with a different instance of C
r4 = weakref.ref(ob, C().__del__)

# Create a proxy reference to ob, using a bound method as the callback
p = weakref.proxy(ob, C().__del__)

# Create a proxy reference to ob, using a bound method as the callback
# but with a different instance of C
