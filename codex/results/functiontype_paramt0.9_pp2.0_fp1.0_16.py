from types import FunctionType
list(FunctionType(str.__dict__['join']).__globals__.keys())

## [out]: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', 
#         'builtins', 'op_add', 'op_contains', 'op_delitem', 'op_getitem', 'op_setitem', 'op_length_hint', 
#         '_Feature']
#                 
                 
                 
                 
                 
                 
                 
                 
from types import MappingProxyType 
list(MappingProxyType({}).__globals__.keys())

## [out]: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', 
#         '_Feature', 'MappingProxyType']
