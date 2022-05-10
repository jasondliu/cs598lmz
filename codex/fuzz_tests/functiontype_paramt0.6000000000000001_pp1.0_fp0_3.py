from types import FunctionType
list(FunctionType(lambda: 0, globals())
     for x in range(3))

# output:
[<function <lambda> at 0x7f6f5c6c5d90>,
 <function <lambda> at 0x7f6f5c6c5e18>,
 <function <lambda> at 0x7f6f5c6c5ea0>]

# not a problem in Python 2:
import sys

if sys.version_info[0] == 2:
    [lambda: 0 for x in range(3)]

# output:
[<function <lambda> at 0x7f6f5c6c5d90>,
 <function <lambda> at 0x7f6f5c6c5e18>,
 <function <lambda> at 0x7f6f5c6c5ea0>]

# or when listcomps are wrapped in parens:
list((FunctionType(lambda: 0, globals())
      for x in range(3)))

# output:
[<function <lambda> at 0x7f6f5c6c5
