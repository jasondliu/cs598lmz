import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# create a list of objects to be collected
lst = []
lst.append(weakref.ref(lst))
lst.append(weakref.ref(lst))
lst.append(weakref.ref(lst))
lst.append(weakref.ref(lst))

# create an object that cannot be collected
class C:
    def __del__(self):
        print "C.__del__"

print gc.get_count()

# create a cycle and force collection
x = C()
lst.append(weakref.ref(x))
lst.append(weakref.ref(x))
lst.append(weakref.ref(x))
lst.append(weakref.ref(x))
lst.append(weakref.ref(x))
lst.append(weakref.ref(x))
lst.append(weakref.ref(x))
lst.append(weakref.ref(x))
lst.append(weakref.ref(x))
lst.append(weakref
