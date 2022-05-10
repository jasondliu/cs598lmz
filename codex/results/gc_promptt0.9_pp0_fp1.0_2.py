import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    def __del__(self):
        pass
# Used when checking finalization
class Bar(object):
    pass

def f():
    l = [Foo(), Bar()]
    del l[1]


gc.collect()
print 'After first collect:'
gc.collect()
print 'After second collect:'
f()
print 'After f():'
gc.collect()
print 'Final collect:'

if gc.garbage:
#    for i in gc.garbage:
#        print i  
    print ('Should be empty:', gc.garbage[0])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
