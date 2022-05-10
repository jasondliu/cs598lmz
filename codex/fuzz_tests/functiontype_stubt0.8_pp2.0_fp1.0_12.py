from types import FunctionType
a = (x for x in [1])
b = FunctionType(
    'lambda x: x',
    (),
    {'__builtins__': __builtins__}
)()
b(a)

"""
"""
>>> g = (x << 1 if x<10 else x + 10 for x in range(20))
>>> isinstance(g, GeneratorType) and inspect.isgenerator(g)
True
>>> g = [x << 1 if x<10 else x + 10 for x in range(20)]
>>> isinstance(g, GeneratorType) and inspect.isgenerator(g)
False
>>>


"""
