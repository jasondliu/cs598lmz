import types
# Test types.FunctionType and types.MethodType, see #12756.
_real_type1 = type(lambda: None)
_real_type2 = type(True.__str__)
if _real_type1 is not _real_type2:
    class FunctionType(_real_type1, _real_type2):
        pass
    class MethodType(_real_type2, _real_type1):
        pass
    types.FunctionType = FunctionType
    types.MethodType = MethodType

try:
    import UserDict
except ImportError:
    from collections import UserDict

import sys

def safe_pickle_dump(obj, path):
    """Dump pickle.dump, creating directory if necesary."""
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d)
    with open(path, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def safe_pickle_load(
