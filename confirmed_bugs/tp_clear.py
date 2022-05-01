import gc, weakref


class LateFin:
    __slots__ = ('ref',)

    def __del__(self):
        # 8. Now `latefin`'s finalizer is called. Here we obtain a reference to
        # `func`, which is currently undergoing `tp_clear`.
        global func
        func = self.ref()


class Cyclic(tuple):
    __slots__ = ()

    # 4. The finalizers of all garbage objects are called. In this case this is
    # only us as `func` doesn't have a finalizer.
    def __del__(self):
        # 5. Create a weakref to `func` now. If we had created it earlier, it
        # would have been cleared by the garbage collector before calling the
        # finalizers.
        self[1].ref = weakref.ref(self[0])
        # 6. Drop the global reference to `latefin`. The only remaining
        # reference is the one we have.
        global latefin
        del latefin
    # 7. Now `func` is `tp_clear`-ed. This drops the last reference to `Cyclic`,
    # which gets `tp_dealloc`-ed. This drops the last reference to `latefin`.


latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

# 1. Create a reference cycle of `cyc` and `func`.
func.__module__ = cyc

# 2. Make the cycle unreachable, but keep the global reference to `latefin` so
# that it isn't detected as garbage. This way its finalizer will not be called
# immediately.
del func, cyc

# 3. Invoke garbage collection, which will find `cyc` and `func` as garbage.
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.collect()
gc.set_debug(0)

# 9. Call `repr()`, which will try to use the NULL `func_qualname`.
repr(func)
