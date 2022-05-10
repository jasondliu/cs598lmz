from types import FunctionType
a = (x for x in [1])
isinstance(a, GeneratorType)

b = (x for x in [1])
isinstance(b, FunctionType)

c = (x for x in [1])
isinstance(c, object)

d = (x for x in [1])
isinstance(d, str)
