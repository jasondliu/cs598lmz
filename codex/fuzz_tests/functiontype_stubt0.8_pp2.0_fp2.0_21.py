from types import FunctionType
a = (x for x in [1])
b = list(a)
c = a.__class__
#assert type(a) == c
#assert isinstance(a, c)
#assert type(a) is not c
#assert type(a) is GeneratorType
#assert isinstance(a, GeneratorType)
#assert type(a) is not IteratorType
#assert isinstance(a, IteratorType)
#assert type(a) is not IterableType
#assert isinstance(a, IterableType)
#assert type(a) is not FunctionType
#assert isinstance(a, FunctionType)
