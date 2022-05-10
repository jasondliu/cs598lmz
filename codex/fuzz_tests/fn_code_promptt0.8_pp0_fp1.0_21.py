fn = lambda: None
# Test fn.__code__.co_varnames. It's a tuple of strings that contains
# only "a" and "b".
a = 1
b = 2
# A function that returns a + b.
fn = lambda a, b: a + b
print(fn.__code__.co_varnames)

# Test fn.__code__.co_argcount. It's an integer that shows the number
# of arguments of a function.
a = 1
b = 2
# A function that returns a + b.
fn = lambda a, b: a + b
print(fn.__code__.co_argcount)

# Test fn.__code__.co_argcount. It's an integer that shows the number
# of arguments of a function.
a = 1
b = 2
# A function that returns a + b.
fn = lambda a, b: a + b
print(fn.__code__.co_argcount)
