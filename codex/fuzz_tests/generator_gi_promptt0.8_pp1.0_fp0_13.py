gi = (i for i in ())
# Test gi.gi_code
gi.gi_code

# Test getting the gi from its code
gi2 = eval(gi.gi_code)
# Test the equality of gi and gi2
gi == gi2

# Test a function
def foo(x):
    def bar(y):
        return x+y
    return bar

# Get the code of the function foo
foo_code = foo.__code__
# Test getting the code of bar
bar_code = foo.__closure__[0].cell_contents.__code__
# Test the equality of bar_code and the first constant in foo_code
bar_code == foo_code.co_consts[0]
# Test the equality of the function bar and the first constant in foo_code
bar == foo_code.co_consts[0]

# Test a function
def foo(x):
    return lambda y: x+y

# Get the code of foo
foo_code = foo.__code__
# Test getting the code of the function foo returns
bar_code = foo_code.co_consts[0].
