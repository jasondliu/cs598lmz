fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can get the code object from a builtin function
import builtins
builtins.__code__

# Test that we can get the code object from a builtin method
import builtins
builtins.__init__.__code__

# Test that we can get the code object from a builtin method
import builtins
builtins.__init__.__func__.__code__

# Test that we can get the code object from a builtin method
import builtins
builtins.__init__.__func__.__code__

# Test that we can get the code object from a builtin method
import builtins
builtins.__init__.__func__.__code__

# Test that we can get the code object from a builtin method
import builtins
builtins.__init__.__func__.__code__

# Test that we can get the code object from a builtin method
import builtins
builtins.__init__.__func__.__code__

# Test that we can get the code object from a builtin method

