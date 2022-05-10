import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f(n):
    if n == 0:
        return 42
    return f(n-1)

print gc.collect()
print gc.collect()
print gc.collect()

def g(n):
    return f(n)

#print gc.collect()
#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()
#print gc.collect()

print g(1)
print g(100)

print gc.collect()
print gc.collect()
print gc.collect()

def h(n):
    if n == 0:
        return 42
    return g(n-1)

print h(1)
print h(100)

print gc.collect()
print gc.collect()
print gc.collect()

def i(n):
    if n == 0:
        return 42
    return i(n-1)

print i(1)
print i(100)

print gc
