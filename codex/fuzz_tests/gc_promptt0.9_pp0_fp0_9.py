import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()                                                        
gc.collect()
print("gc.garbage:", gc.garbage)
# Define a weakref callback function
def callback(reference):                                                    
    print("Calling back", reference)
# Create a weakref to an arbitrary object                                        
r = weakref.ref(dict(abc=123), callback)                                              
# Verify that the callback works                                                     
d = r()                                                                              
print("ref->dict before:", d)
d["abc"] = 456
print("ref->dict after:", d)
# Delete the object to force the callback                                           
del d                                                                               
print("ref->dict after:", r())
# No object is referenced by r anymore                                           
print("Ref attributes -- ref object:", r, "refcount:", gc.get_refcount(r), "callback:", r.__init__.__defaults__[0])
del r
print("ref attributes:", r)
d = gc.garbage.pop()
print("ref attributes:", r)
print("d
