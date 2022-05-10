from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# ['x', 'y', 'z']

# The following code uses the inspect module to extract the names of the
# arguments of a function:

from inspect import getfullargspec
getfullargspec(lambda x, y, z: None).args

# ['x', 'y', 'z']

# The following code uses the ast module to extract the names of the arguments
# of a function:

from ast import parse
parse('lambda x, y, z: None').body.args.args

# [<_ast.Name object at 0x7f4e6f0c6a90>,
#  <_ast.Name object at 0x7f4e6f0c6b10>,
#  <_ast.Name object at 0x7f4e6f0c6b90>]

# The following code uses the ast module to extract the names of the arguments
# of a function:

from ast import parse
parse('lambda x, y, z: None').body.args.args

# [
