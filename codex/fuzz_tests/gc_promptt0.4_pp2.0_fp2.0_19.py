import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Test a cyclic list
l = []
l.append(l)
print(gc.collect())

# Test a cyclic dict
d = {}
d[0] = d
print(gc.collect())

# Test a cyclic tuple
t = (1,)
t += (t,)
print(gc.collect())

# Test a cyclic class
class C:
    pass
c = C()
c.a = c
print(gc.collect())

# Test a cyclic instance
class D:
    def __init__(self):
        self.a = self
d = D()
print(gc.collect())

# Test a cyclic instance with a __del__ method
class E:
    def __init__(self):
        self.a = self
    def __del__(self):
        pass
e = E()
print(gc.collect())

# Test a cyclic list with a __del__ method
class F:
    def __del__(self):
        pass
l = []
l.append(F())
l.
