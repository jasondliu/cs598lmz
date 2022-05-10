from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

#%%
import dis
dis.dis(lambda: None)

#%%
def make_adder(n):
    return lambda x: x + n

add_3 = make_adder(3)
add_3(4)

#%%
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_3 = make_adder(3)
add_3(4)

#%%
def make_adder(n):
    return lambda x: x + n

add_3 = make_adder(3)
add_3(4)

#%%
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_3 = make_adder(3)
add_3(4)

#%%
def
