from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# [<function <lambda> at 0x7f8e8c0d8f28>, <function <lambda> at 0x7f8e8c0d8ea0>]

# We can also use the inspect.getsource() function to get the source code of a function:

from inspect import getsource
getsource(lambda x: x)

# 'lambda x: x\n'

# We can also use the inspect.getclosurevars() function to get the variables that a function closes over:

from inspect import getclosurevars
getclosurevars(lambda x: x)

# ClosureVars(nonlocals={}, globals={...}, builtins={...}, unbound=set())

# We can also use the inspect.getfile() function to get the file that a function was defined in:

from inspect import getfile
getfile(lambda x: x)

# '<ipython-input-2-f8e9c3c3b6f3>'

# We can also use the inspect.get
