from types import FunctionType
list(FunctionType(lambda a: 3, {}).__code__.co_freevars)

import dis
def f():
    a = 1
    b = 2
    c = 3
    c = a + b

dis.dis(f)

#%%
from types import FunctionType
def make_adder(x):
    def adder(y):
        return x + y
    return adder

make_adder(3)(4)

add_three = make_adder(3)
add_three(4)

#%%
def make_adder(x):
    def adder(y):
        return x + y 
    return adder

adder_three = make_adder(3)
adder_five = make_adder(5)

adder_three(4)
adder_five(4)

#%%
def make_adder(x):
    def adder(y):
        return x + y 
    return adder

adder_three = make_adder(3)
adder_five = make_adder(5)

make_adder(3)(4
