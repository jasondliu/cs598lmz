import weakref
# Test weakref.ref
# Create a cycle and then break it
def f():
    l = [1, 2, 3]
    return weakref.ref(l)

def g():
    x = f()
    print(x)
    print(x())
    return x

r = g()
print(r)
print(r())
r = None
print(r)
print(r())
print(g())
print(g()())
print(f())
print(f()())
