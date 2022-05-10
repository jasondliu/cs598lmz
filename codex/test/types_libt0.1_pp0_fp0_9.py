import types
types.MethodType(lambda self: None, None, Dummy)

# do not import *
from types import *

# (don't check in other tests -- see explanation above)
TestJyNI.test_import_star()

# do not import * from __future__
