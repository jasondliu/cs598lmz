from types import FunctionType
list(FunctionType(add.__code__, globals(), "add"))

#%%

def add(x:int,y:int) -> int:
    return x+y

TypeError: 'NoneType' object is not callable

#%%
