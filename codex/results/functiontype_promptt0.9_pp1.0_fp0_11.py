import types
# Test types.FunctionType
from types import FunctionType
from sys import getrefcount
FunctionType([object], object)
isinstance(FunctionType, type)
isinstance(FunctionType, object)
FunctionType.mro()
FunctionType([object], object)
del FunctionType
# Test types.LambdaType
from types import LambdaType
from sys import getrefcount
LambdaType([object], object)
isinstance(LambdaType, type)
isinstance(LambdaType, object)
LambdaType.mro()
LambdaType([object], object)
del LambdaType
# Test types.GeneratorType
from types import GeneratorType
from sys import getrefcount
GeneratorType([object], object)
isinstance(GeneratorType, type)
isinstance(GeneratorType, object)
GeneratorType.mro()
GeneratorType([object], object)
del GeneratorType
# Test types.GeneratorType
from types import GeneratorType
from sys import getrefcount
GeneratorType([object], object)
isinstance(GeneratorType, type)
isinstance(GeneratorType
