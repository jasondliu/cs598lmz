fn = lambda: None
# Test fn.__code__.co_varnames contains "self", "fn" and "x"
# so that sum(fn.__code__.co_varnames) == "selfselffnx"
def gen_fn():
    def fn(self, x):
        return x
    return fn
fn = gen_fn()
class Obj(object):
    @fn
    def f(self, x):
        return x

o = Obj()
print(o.f(5))

# Exercise 2
# Write a function that takes a function as an argument
# and returns a function that wraps that function to 
# print its argument and then call the original function
def trace(f):
    def wrapped(x):
        print('Calling', f.__name__, 'on argument', x)
        return f(x)
    return wrapped

@trace
def square(x):
    return x * x

print(square(5))
print(square(2))

# Exercise 3
# Count the number of times a function is called
def countcalls(f):
    def wrapped(*args):

