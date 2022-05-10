from types import FunctionType
a = (x for x in [1])
a.__iter__

type((x for x in [1]))
type(a)
type(lambda: None)
FunctionType

a = range(1, 5)
a.__aiter__ = iter

type(a.__aiter__)
type(a.__iter__)

type(a.__iter__())

type(a.__iter__())
type(a.__aiter__())

##jupyter
import types
class my_aiter:
    def __aiter__(self):
        return iter([1, 2, 3])
        
a1 = my_aiter()

isinstance(my_aiter, types.GeneratorType)
isinstance(a1.__aiter__, types.GeneratorType)
isinstance(a1.__aiter__(), types.GeneratorType)

class my_aiter2:
    async def __aiter__(self):
        return iter([1, 2, 3])
        
class my_aiter3:
    async def __aiter__(self):
