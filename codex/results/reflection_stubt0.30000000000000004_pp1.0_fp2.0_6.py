fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #29054: Ensure that the __code__ attribute of a builtin function
# is not set to a non-code object.
import builtins
builtins.__dict__['__code__'] = 42

# Issue #29054: Ensure that the __code__ attribute of a builtin method
# is not set to a non-code object.
import builtins
builtins.__dict__['__code__'] = 42

# Issue #29054: Ensure that the __code__ attribute of a builtin method
# is not set to a non-code object.
import builtins
builtins.__dict__['__code__'] = 42

# Issue #29054: Ensure that the __code__ attribute of a builtin method
# is not set to a non-code object.
import builtins
builtins.__dict__['__code__'] = 42

# Issue #29054: Ensure that the __code__ attribute of a builtin method
# is not set to a non-code object.
import builtins
builtins.__dict__['__
