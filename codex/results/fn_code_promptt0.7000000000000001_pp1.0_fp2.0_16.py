fn = lambda: None
# Test fn.__code__.co_varnames
#
# fn.__code__.co_varnames is a tuple containing the names of the
# variables created by the code object.

def fn(a, b):
    return a, b

print(fn.__code__.co_varnames)

def fn(a, b):
    print('a', a)
    print('b', b)

print(fn.__code__.co_varnames)

def fn(a, b):
    c = a + b
    return c

print(fn.__code__.co_varnames)

fn = lambda a, b: a + b
print(fn.__code__.co_varnames)

# Test fn.__code__.co_argcount
#
# fn.__code__.co_argcount is the number of positional-or-keyword
# arguments (including arguments with default values) accepted by the
# code object.

def fn():
    pass

print(fn.__code__.co_argcount)

def
