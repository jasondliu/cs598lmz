from types import FunctionType
list(FunctionType(lambda _:_).__code__.co_varnames)
 
#%%
from types import MappingProxyType
from types import MappingProxyType
p = {'name': 'aaa'}
m = MappingProxyType(p)
m['name']
m['name'] = 'bbb'
m['name']
p['name']
p['name'] = 'bbb'
m['name']
 
#%%
# 类型标识
from types import DynamicClassAttribute
DynamicClassAttribute


#%%
