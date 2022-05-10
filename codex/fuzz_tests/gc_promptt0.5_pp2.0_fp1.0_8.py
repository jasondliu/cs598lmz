import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __del__(self):
        print "collecting A"
        gc.collect()

a = A()
del a
gc.collect()
# Test gc.collect()
class A:
    def __del__(self):
        print "collecting A"
        gc.collect()

class B:
    def __del__(self):
        print "collecting B"

a = A()
b = B()
del a
del b
gc.collect()
# Test gc.collect()
class A:
    def __del__(self):
        print "collecting A"
        gc.collect()

class B:
    def __del__(self):
        print "collecting B"

a = A()
b = B()
del a
del b
gc.collect()
# Test gc.collect()
class A:
    def __del__(self):
        print "collecting A"
        gc.collect()

class B:
    def __del__(self):
       
