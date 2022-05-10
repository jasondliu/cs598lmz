from types import FunctionType
list(FunctionType(14))
#Inconsistent with its name as FunctionType is a type and list() is for converting  any iterable to a list

#4
from types import FunctionType
from string import ascii_letters
FunctionType.mro()[1].__subclasses__(ascii_letters)
# FunctionType is an abstract class and it does not have __subclasses__-method

#5
from types import FunctionType
from decimal import Decimal
FunctionType.mro()[1](Decimal(33))
#FunctionType is an abstract class and it cannot be called as there is no body associated with it

#6
from types import FunctionType
from types import ModuleType
from fractions import Fraction
FunctionType.mro()[1](ModuleType("Fractions"), Fraction(11))
#FunctionType is an abstract class and it cannot be called as there is no body associated with it

#7
from types import FunctionType
from collections import OrderedDict
FunctionType.mro()[1](OrderedDict(int, str), "Sree")
#FunctionType is an abstract class and it
