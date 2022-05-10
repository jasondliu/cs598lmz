import types
# Test types.FunctionType (used by others)
assert(type(f) == types.FunctionType)

# Tests GLOBAL
my_global = 1

def change_global():
    global my_global
    my_global = 2

def use_global():
    return my_global

change_global()
assert(use_global() == 2)

# Test CLOSURE
def make_adder(n):
    def add(x):
        return x + n
    return add

adder1 = make_adder(1)
adder10 = make_adder(10)

assert(adder1(100) == 101)
assert(adder10(100) == 110)

# TEST DECORATOR

def decorator(f):
    def decorated(x):
        print ' Doing f(x) with x=', x
        return f(x)
    return decorated

def f(x):
    return x + 10

g = decorator(f)
assert(g(1) == 11)

# TEST DECORATOR WITH ARGS

def decorator_args(arg):
