import weakref
# Test weakref.ref()

def f(x):
    return lambda: x

r = weakref.ref(f(1))
print(r())
print(r()())

r = weakref.ref(f(2))
print(r())
print(r()())

r = weakref.ref(f(3))
print(r())
print(r()())

r = weakref.ref(f(4))
print(r())
print(r()())

r = weakref.ref(f(5))
print(r())
print(r()())

r = weakref.ref(f(6))
print(r())
print(r()())

r = weakref.ref(f(7))
print(r())
print(r()())

r = weakref.ref(f(8))
print(r())
print(r()())

r = weakref.ref(f(9))
print(r())
print(r()())

r = weakref.ref(f(10))
print(r())
print(r()())

