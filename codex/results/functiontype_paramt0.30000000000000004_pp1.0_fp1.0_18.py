from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# This is a bit of a hack, but it works.

# The function's code object has a co_varnames attribute, which is a tuple of
# the names of the arguments.

# In Python 3.3 and later, you can use the inspect.signature() function to get
# the same information.

import inspect
inspect.signature(lambda x, y: x + y).parameters

# OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])

# Last updated: 2017-02-14
# Written by: Matt Harrison
