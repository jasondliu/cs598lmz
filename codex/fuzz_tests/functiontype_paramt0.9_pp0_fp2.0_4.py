from types import FunctionType
list(FunctionType(lambda x: x*10, globals()) for i in range(5))

#无参数
def no_args():
    pass

def required_arg(name):
    print( name )

def arg_with_default(name, age=20):
    print( name,age )

def multi_args(name, *args):
    print( name, args)

def kwargs_args(name, **kargs):
    print( name, kargs)

def multi_args_kwargs(name, *args, **kargs):
    print( name, args, kargs)

#导入
import math
from math import pi, sqrt

import math as m
import math, sys
from math import pi as Pi
from math import *
#习惯写法
from foo.bar.yourclass import YourClass
#不安全的写法
from foo.bar import *

paths = [__file__, 
         'README.md', 
         __file__.split
