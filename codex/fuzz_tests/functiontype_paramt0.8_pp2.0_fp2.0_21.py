from types import FunctionType
list(FunctionType(res).__code__.co_varnames[1:])

#%%
from types import FunctionType
list(FunctionType(res).__code__.co_varnames[1:])[1:3]

#%%
from types import FunctionType
from functools import reduce
liste = 1,2,3,4,5
def mult(a,b):
    return a*b
print(reduce(mult,liste))

#%%
from types import FunctionType
from functools import reduce
from math import sqrt
def distance(a,b):
    return sqrt(a+b)
print(reduce(distance,1))

#%%
from types import FunctionType
from functools import reduce
from math import sqrt
def distance(a,b):
    return sqrt(a+b)
print(reduce(distance,(1,0,5,5)))

#%%
from types import FunctionType
from functools import reduce
from math import sqrt
def distance(a,b):
    return sqrt(a+b
