from types import FunctionType
list(FunctionType(mi_funcion.func_code,globals(),"funcion_unitaria",('s',),mi_funcion.func_defaults))

# zip

list(zip("abcd","xyz"))

# filter

list(filter(lambda x: x > 0,[-1,3,5,-6]))

# reduce

from functools import reduce

reduce(lambda x,y: int(x)+int(y),'12')

# lambda

list(map(lambda x: x**2, [1,2,3,4]))
list(filter(lambda x: x > 0,[-1,3,5,-6]))
from functools import reduce
reduce(lambda x,y: int(x)+int(y),'12')

# Módulo operator

from operator import mul, add
from functools import reduce
reduce(add, [1,2,3,4])

# Módulo itertools
from itertools import *

# permutations

from itertools import perm
