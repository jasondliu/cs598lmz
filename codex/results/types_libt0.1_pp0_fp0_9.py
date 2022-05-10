import types
types.MethodType(lambda self: None, None, Dummy)

# do not import *
from types import *

# (don't check in other tests -- see explanation above)
TestJyNI.test_import_star()

# do not import * from __future__
from __future__ import division, absolute_import, print_function

# do not use exec
exec 'print(42)' in {}

# do not use eval
eval('2+3')

# do not use apply
apply(pow, (2, 4))

# do not use reduce
reduce(lambda x, y: x+y, range(10))

# do not use reload
reload(sys)

# do not use intern
s = intern('Qux')

# do not use buffer
buffer('abc')

# do not use coerce
coerce(1, 1.0)

# do not use callable
callable(int)

# do not use file
file('abc')

# do not use execfile
execfile('abc')

# do not use
