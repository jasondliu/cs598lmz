from types import FunctionType
a = (x for x in [1])
type(a)

type(lambda x:x) == FunctionType

import types

def fn():
    pass

type(fn) == types.FunctionType

type(abs) == types.BuiltinFunctionType
type(lambda x:x) == types.LambdaType
type((x for x in range(1))) == types.GeneratorType

# isinstance
isinstance(fn, FunctionType)

# dir
dir(fn)
