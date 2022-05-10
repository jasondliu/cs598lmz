from types import FunctionType
list(FunctionType(lambda x: x % 2, globals()))

#---------------------------------------------------------------------------------------------------
# This is a function that returns a function
#---------------------------------------------------------------------------------------------------

def make_adder(n):
    def add(x):
        return x + n
    return add

add3 = make_adder(3)
add3(4)

#---------------------------------------------------------------------------------------------------
# This is a function that returns a function
#---------------------------------------------------------------------------------------------------

def make_adder(n):
    return lambda x: x + n

add3 = make_adder(3)
add3(4)

#---------------------------------------------------------------------------------------------------
# This is a closure
#---------------------------------------------------------------------------------------------------

def make_adder(n):
    def add(x):
        return x + n
    return add

f = make_adder(3)
f(4)
f(5)

def make_adder(n):
    def add(x):
        return x + n
    return add

add3 = make_adder(3)
add5 = make_adder(5)
add3(4)
add5(4)


