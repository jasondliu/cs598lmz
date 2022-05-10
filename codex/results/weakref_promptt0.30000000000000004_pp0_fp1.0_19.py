import weakref
# Test weakref.ref() on a class instance.
class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

# Test weakref.proxy() on a class instance.
p = weakref.proxy(o)
print(p)
print(p is o)

# Test weakref.proxy() on a builtin type.
p = weakref.proxy(list)
print(p)
print(p is list)

# Test weakref.proxy() on a builtin function.
p = weakref.proxy(len)
print(p)
print(p is len)

# Test weakref.proxy() on a builtin method.
p = weakref.proxy([].append)
print(p)
print(p is [].append)

# Test weakref.proxy() on a builtin class.
p = weakref.proxy(int)
print(p)
print(p is int)

# Test weakref.proxy() on a module.
import sys
p = weakref
