from types import FunctionType
list(FunctionType(x.__code__,globals(),'my_func'))

def my_func():
    a = 1
    b = 2
    c = 3
    return a,b,c

my_func.__code__.co_consts

my_func.__code__.co_varnames

my_func.__code__.co_names

my_func.__code__.co_nlocals

my_func.__code__.co_stacksize

my_func.__code__.co_flags

import dis
dis.dis(my_func)

import inspect
inspect.getsource(my_func)

inspect.getsourcelines(my_func)

inspect.getcomments(my_func)

import sys
sys.modules

sys.modules['os']

sys.modules['os'].path

sys.modules['os'].path.join('usr','bin','spam')

import os
os.path.join('usr','bin','spam')

os.getcwd
