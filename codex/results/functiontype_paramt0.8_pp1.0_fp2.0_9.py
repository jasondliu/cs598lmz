from types import FunctionType
list(FunctionType(lambda: None, {}).__closure__)

# 来源
# https://stackoverflow.com/questions/1301346/get-the-name-of-an-objects-type-in-python


# class
print(type(ClassA).__name__)

# function
fun = lambda: 1
print(type(fun).__name__)

# instance
print(type(ClassA()).__name__)

# type
print(type(type(ClassA)).__name__)

# module
import sys
print(type(sys).__name__)

# builtin_function_or_method 
print(type(list).__name__)

# method_descriptor 
print(type(list.__add__).__name__)

# getsource
import inspect
print(inspect.getsource(ClassA))

# Function
print(dir(FunctionType))

# Method
print(dir(type.__call__))

# Module
import builtins
print(dir(builtins))


