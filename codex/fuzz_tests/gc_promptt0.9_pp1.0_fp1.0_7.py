import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with get_referents

class A:
    def __init__(self, arg):
        self.b = arg

a = A(1)
x = set()
refs = gc.get_referents(a)
for r in refs:
    x.add(r)
print(x)
del a
gc.collect()
print(x)
# Test gc.get_referents to make sure they dont
# include the original object itself

class A:
    def __init__(self, x):
        self.x = x

a = A(1)
refs = gc.get_referents(a)
if a in refs:
    print("Error: get_referents")

class A:
    def __init__(self, x):
        self.x = x

    def __del__(self):
        pass

a = A(1)
refs = gc.get_referents(a)
if a not in refs:
    print("Error: get_referents
