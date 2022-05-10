fn = lambda: None
# Test fn.__code__.co_firstlineno after the outer function has already
# returned.
def f():
    def g():
        return 1
    x = g()
    return x
f()

p = _get_code_object(f).co_firstlineno

if p != __name__ + '.f.<locals>.g':
    raise RuntimeError

if x != 1:
    raise RuntimeError

# Check that we actually get the code object.
def outer():
    def f():
        print(f.__code__)
        print(f.__code__.co_argcount)
    f()
    print(f.__code__)
    print(f.__code__.co_argcount)

outer()

try:
    outer.__code__.co_varnames
except AttributeError:
    print("OK")
else:
    raise RuntimeError

def g():
    print(g.__code__.co_varnames, g.__code__.co_argcount)
g()

# Check that we can pass co_
