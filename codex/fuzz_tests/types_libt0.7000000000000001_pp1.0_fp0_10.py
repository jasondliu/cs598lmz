import types
types.ModuleType
import sys
sys.modules
sys.modules['sys']

import types
def get_module_attr(module, attr):
    if not isinstance(module, types.ModuleType):
        raise TypeError(f"Provided module is not a module")
    if not hasattr(module, attr):
        raise ValueError(f"Module has no attribute '{attr}'")
    return getattr(module, attr)

import numbers
numbers.Integral

# %%
import types

def get_module_attr(module, attr):
    if not isinstance(module, types.ModuleType):
        raise TypeError(f"Provided module is not a module")
    if not hasattr(module, attr):
        raise ValueError(f"Module has no attribute '{attr}'")
    return getattr(module, attr)

import numbers
get_module_attr(numbers, "Integral")

# %%
import types

def get_module_attr(module, attr):
    if not isinstance(module, types
