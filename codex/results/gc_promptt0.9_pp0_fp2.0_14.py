import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() for garbage-collected objects with __del__
# methods which don't use kind macros

# A class using INST_SLOT
class A:
    def __init__(self, value):
        self.value = value

    def __del__(self):
        global A_del
        A_del += 1


a = A(12)
a_weakref = weakref.ref(a)
a = A_del = None
gc.collect(); gc.collect(); gc.collect(); gc.collect(); gc.collect()

# Three objects are left:
# - A_del is a PyIntObject, to track the number of collected A's
# - a_weakref is a KeyedRef object
# - <garbage collected> is the KeyedRef's key (an A object).
# All objects created by this class are collected.

# A class using PIC
class B(list):
    def __init__(self, value):
        self.value = value

    def __del__(self):
        global B_del
        B_del += 1


