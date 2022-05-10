from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_varnames)

#%%
from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_varnames)

#%%
from types import FunctionType
list(FunctionType(lambda x, y: (x, y), {}).__code__.co_varnames)

#%%
from types import FunctionType
list(FunctionType(lambda x=1, y=2: (x, y), {}).__code__.co_varnames)

#%%
from types import FunctionType
list(FunctionType(lambda *args: args, {}).__code__.co_varnames)

#%%
from types import FunctionType
list(FunctionType(lambda **kwargs: kwargs, {}).__code__.co_varnames)

#%%
from types import FunctionType
list(FunctionType(lambda *args, **kwargs: (args, kwargs), {}).__code__.co_varnames)

#%%
from types import FunctionType
list
