import types
# Test types.FunctionType
def function0():
    return 0
# Test all types
def function1(a,b,c):
    return a,b,c

assert(isinstance(function0, types.FunctionType))
assert(isinstance(function1, types.FunctionType))

import lib_util

# Returns None if key is not in dictionary.
def DictGetKey(dict, key):
    if key in dict:
        return dict[key]
    return None

# Exemple of use: DictGetKey(paramDict, "x")

def DictFilter(paramDict, names):
    """Retain only the parameters which names are in the list of names.
    Their order is kept as in this list.
    This is used to relate to SQL columns, which are also in a given order."""
    return [ DictGetKey(paramDict, name) for name in names ]
