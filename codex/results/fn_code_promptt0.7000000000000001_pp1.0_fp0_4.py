fn = lambda: None
# Test fn.__code__.co_varnames

def f():
    a, b, c = 1, 2, 3
    return a, b, c

print(f())
print(f.__code__.co_varnames)

fn.__code__.co_varnames = f.__code__.co_varnames
print(fn())
