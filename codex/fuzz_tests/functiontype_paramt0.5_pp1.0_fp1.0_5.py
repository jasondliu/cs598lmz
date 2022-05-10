from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), "f")(10))

# But this is more useful:
def f(x):
    return x+1

# And this is even more useful:
def g(x):
    return x+1

g(10)

# We can even assign functions to variables:
h = g
h(10)

# We can also pass functions as arguments to other functions:
def apply_function(f, x):
    return f(x)

apply_function(g, 10)

# And we can return functions from other functions:
def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(2)
f(10)

# We can also define functions with a variable number of arguments:
def varargs(*args):
    return args

varargs(1, 2, 3)

# Or keyword arguments:
def keyword_args(**kwargs):
    return kwargs

keyword_args(big="foot", loch="ness")

# We can
