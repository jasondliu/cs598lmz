import weakref
# Test weakref.ref on built-in types

def f(x):
    return str(len(x))

w = weakref.WeakMethod(f)

if w() != '1':
    raise RuntimeError
