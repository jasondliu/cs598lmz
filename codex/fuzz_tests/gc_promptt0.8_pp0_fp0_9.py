import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class C(object):
    def __init__(self,name):
        self.__name = name
    def name(self):
        return self.__name

# Creating objects
a = C('a')
b = C('b')
c = C('c')

# Creating a cycle
a.b = b
b.c = c
c.a = a

# Creating a weakref to the object
wr = weakref.ref(a)

# Fetching a name twice to check that the object exists
print wr().name()
print wr().name()

del a,b,c
gcol = gc.collect()
print gcol, "unreachable objects found"
#wr().name()

#if gcol:
    #print wr().name()
    #print wr()
    #print wr().name()
    #print wr().name()
    #wr().name()

#print wr(), wr() is None

#weakref_callback.py
import gc, weakref
gc.set_debug(gc.DEBUG_LEAK)
