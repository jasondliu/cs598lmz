from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

#%%
from types import FunctionType
FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__)

#%%
from types import FunctionType
FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__)(1,2)

#%%
from types import FunctionType
FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__)(1,2)

#%%
from types import FunctionType
FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f
