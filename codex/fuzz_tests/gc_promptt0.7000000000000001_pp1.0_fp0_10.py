import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
def func():
    class C:
        pass
    o = C()
    o2 = o.__class__
    del o
    gc.collect()
    print(o2)

func()

# Test gc.collect() with a __del__ method.
def func():
    class C:
        def __del__(self):
            pass
    o = C()
    del o
    gc.collect()

func()

# Test gc.collect() with cyclic garbage.
def func():
    l = []
    l.append(l)
    del l
    gc.collect()

func()

# Test gc.collect() with a __del__ method that resurrects the object.
def func():
    class C:
        def __del__(self):
            self.o = self
    o = C()
    del o
    gc.collect()

func()

# Test gc.collect() with a __del__ method that resurrects the object and
# creates a cycle.
def func():
   
