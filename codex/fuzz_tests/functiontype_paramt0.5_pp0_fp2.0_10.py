from types import FunctionType
list(FunctionType(lambda x:x,globals(),'func').__code__.co_freevars)

#%%
from types import FunctionType
list(FunctionType(lambda x:x,globals(),'func').__code__.co_varnames)

#%%
from types import FunctionType
list(FunctionType(lambda x:x,globals(),'func').__code__.co_cellvars)

#%%
from types import FunctionType
list(FunctionType(lambda x:x,globals(),'func').__code__.co_names)

#%%
from types import FunctionType
list(FunctionType(lambda x:x,globals(),'func').__code__.co_consts)

#%%
from types import FunctionType
list(FunctionType(lambda x:x,globals(),'func').__code__.co_lnotab)

#%%
from types import FunctionType
FunctionType(lambda x:x,globals(),'func').__code__.co_stacksize

#%%
from types import FunctionType

