import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    f = Foo()
    f.x = 1
    f.y = 2
    f.z = 3
    return f

def baz():
    f = bar()
    f.x = 4
    f.y = 5
    f.z = 6
    return f

def test():
    f = baz()
    f.x = 7
    f.y = 8
    f.z = 9
    return f

f = test()
f.x = 10
f.y = 11
f.z = 12

print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect
