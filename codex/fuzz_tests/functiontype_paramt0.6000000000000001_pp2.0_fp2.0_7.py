from types import FunctionType
list(FunctionType(f.__code__, globals())(1,2))

#%%
import types
f = lambda x: x+1
print(isinstance(f, types.FunctionType))

#%%
f = lambda x: x+1
def f():
    return x+1
g = lambda x,y,z: x+y+z
def g(x,y,z):
    return x+y+z

#%%
def make_adder(n):
    return lambda x: x + n

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))

#%%
def make_adder(n):
    def adder(x):
        return x + n
    return adder

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))

#%%
def make_adder(n):
    return lambda x: x +
