from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# 从下面这个模块中导入函数
from math import sin, cos, tan

# 导入模块中所有的函数
from math import *

# 导入模块中所有的函数，并且将它们的名称改为原来的名称加上前缀
from math import *

# 导入模块中的函数，并且将它们的名称改为原来的名称加上前缀
from math import sin as my_sin

# 导入模块中的函数，并且将它
