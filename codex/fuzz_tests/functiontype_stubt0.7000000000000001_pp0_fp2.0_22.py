from types import FunctionType
a = (x for x in [1])

if type(a) == GeneratorType:
    print("a is generator")
else:
    print("a is not generator")
