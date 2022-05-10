import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __del__(self):
        pass

class B:
    pass

wr = weakref.ref(A())
wr = weakref.ref(B())

gc.garbage.append(A())
gc.garbage.append(B())

gc.collect()

gc.garbage.append(A())
gc.garbage.append(B())
gc.garbage.append(A())
gc.garbage.append(B())

gc.collect()

gc.garbage.append(A())
gc.garbage.append(A())
gc.garbage.append(A())
gc.garbage.append(B())
gc.garbage.append(B())
gc.garbage.append(B())

gc.collect()

gc.garbage.append(A())
gc.garbage.append(A())
gc.garbage.append(A())
gc.garbage.append(A())
gc.garbage.append(A())
gc.garbage.append(A())
gc.garbage.append
