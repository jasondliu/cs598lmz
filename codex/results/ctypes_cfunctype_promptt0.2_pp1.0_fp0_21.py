import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import *

# Simple function
def func(a, b):
    return a + b

# Function with default argument
def func_default(a, b=1):
    return a + b

# Function with keyword argument
def func_keyword(a, b=1):
    return a + b

# Function with varargs
def func_varargs(*args):
    return sum(args)

# Function with keyword varargs
def func_keyword_varargs(**kwargs):
    return sum(kwargs.values())

# Function with both varargs and keyword varargs
def func_both_varargs(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

# Function with annotation
def func_annotation(a: int, b: int) -> int:
    return a + b

# Function with annotation and default argument
def func_annotation_default(a: int, b: int = 1) -> int:
    return a + b

# Function with annotation and keyword argument

