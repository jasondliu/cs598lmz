from types import FunctionType
list(FunctionType(FunctionType.func_code, {}, None).__globals__.keys())

"""

import inspect
import sys

def get_globals(function):
    return inspect.getclosurevars(function).globals

def get_globals_name(function):
    return list(get_globals(function).keys())

def get_globals_name_and_value(function):
    return {k: v for k, v in
            get_globals(function).items() if not k.startswith('_')}

def get_globals_value(function):
    return list(get_globals_name_and_value(function).values())

def get_globals_value_and_name(function):
    return {v: k for k, v in
            get_globals_name_and_value(function).items()}

def get_globals_name_and_value_except_self(function):
    globals_ = get_globals(function)
    if
