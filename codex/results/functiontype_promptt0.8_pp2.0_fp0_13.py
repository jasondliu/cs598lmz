import types
# Test types.FunctionType
def add_integers(a, b):
    return a + b

type(add_integers)
 
# Test types.LambdaType
lst = [lambda x: x ** 2,
       lambda x: x ** 3,
       lambda x: x ** 4]

type(lst[0])
 
type(lst[1])

 
# Test type.GeneratorType
def infinite_sevens():
    while True:
        yield 7

type(infinite_sevens())
 
# Test types.BuiltinFunctionType
sum([1, 2, 3])

type(sum)
 
# Test isinstance
isinstance(add_integers, types.FunctionType)

isinstance(lst[0], types.FunctionType)

isinstance(infinite_sevens, types.FunctionType)

isinstance(sum, types.BuiltinFunctionType)

isinstance(add_integers, types.LambdaType)

 
# Test types.MethodType
class Adder:
    def __init__(self, n
