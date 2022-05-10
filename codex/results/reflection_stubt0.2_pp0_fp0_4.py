fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #17095: test that the __code__ attribute of a builtin function
# is a code object.
import builtins
assert isinstance(builtins.abs.__code__, types.CodeType)

# Issue #17095: test that the __code__ attribute of a builtin method
# is a code object.
import os
assert isinstance(os.stat.__code__, types.CodeType)

# Issue #17095: test that the __code__ attribute of a builtin method
# is a code object.
import os.path
assert isinstance(os.path.exists.__code__, types.CodeType)

# Issue #17095: test that the __code__ attribute of a builtin method
# is a code object.
import sys
assert isinstance(sys.getrefcount.__code__, types.CodeType)

# Issue #17095: test that the __code__ attribute of a builtin method
# is a code object.
import time
assert isinstance(time.time.__code__, types
