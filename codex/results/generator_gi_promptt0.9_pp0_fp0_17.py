gi = (i for i in ())
# Test gi.gi_code must not be None
# https://bugs.python.org/issue31937#msg310609
import sys, types
assert isinstance(types.SimpleNamespace(), type)
# Type of frames created by types.SimpleNamespace are special; some C
# code (e.g. PyEval_EvalFrameEx) may not work with them.
#
# Note: I had to list types.SimpleNamespace explicitly in the isinstance()
# expression, as "type" matches, which seems to be a general problem:
# File "/usr/lib64/python3.3/functools.py", line 388, in __subclasscheck__
# and issubclass(subtype, self):
if sys.flags.optimize < 2 and isinstance(sys._getframe().f_code, type):
    assert isinstance(sys._getframe().f_code, types.CodeType), type(sys._getframe().f_code)

# Test __subclasses__
subclasses = [subclass for subclass in type.__subclasses__() if subclass.__name__ == "SimpleNamespace"]
assert len
