from types import FunctionType
list(FunctionType(f.__code__,globals(),name='myfunc'))

#%%
from types import FunctionType
f = lambda x:x+1
g = FunctionType(f.__code__,globals(),name='myfunc')
print(g(1))

#%%
from types import FunctionType
f = lambda x:x+1
g = FunctionType(f.__code__,globals(),name='myfunc')
print(g(1))

#%%
from types import FunctionType
f = lambda x:x+1
g = FunctionType(f.__code__,globals(),name='myfunc')
print(g(1))

#%%
from types import FunctionType
f = lambda x:x+1
g = FunctionType(f.__code__,globals(),name='myfunc')
print(g(1))

#%%
from types import FunctionType
f = lambda x:x+1
g = FunctionType(f.__code__,globals(),name='myfunc')
print(g(1))

#%%
