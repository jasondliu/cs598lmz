from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in (lambda: None))

# Test that we can create a function with a closure.
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add1 = make_adder(1)
add1(2)

# Test that we can create a function with a closure that references a
# cell.
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add1 = make_adder(1)
add1(2)

# Test that we can create a function with a closure that references a
# cell that references a cell.
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add1 = make_adder(1)
add1(2)

# Test that we can create a function with a
