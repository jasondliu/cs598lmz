from types import FunctionType
list(FunctionType(lambda : 0, {}, '', (), None, None))

# As an extension to Python, CPython's pickle module can pickle and unpickle
# function objects.  You must import the copy_reg module in order to unpickle
# them, and you must have defined the function with a global statement.  Here's
# an example.

import copy_reg, pickle
def pickle_function(function):
    return unpickle_function, (function.func_code, function.func_globals)

def unpickle_function(code, globals):
    return FunctionType(code, globals)

copy_reg.pickle(FunctionType, pickle_function, unpickle_function)

def constantly(value):
    return lambda : value

# the following will happen with Python 2.2 and 2.3
# f = constantly(42)
# pickled = pickle.dumps(f)
# g = pickle.loads(pickled)
# g()
# 42

# this will happen with Python 2.2, but not with Python 2.3
# f
