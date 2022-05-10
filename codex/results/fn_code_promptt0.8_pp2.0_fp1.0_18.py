fn = lambda: None
# Test fn.__code__.co_names
# fn.__code__.co_names = tuple()

# Test fn.__code__.co_varnames
# fn.__code__.co_varnames = tuple()

# Test fn.__code__.co_filename
import os
_ = os.path.split(fn.__code__.co_filename)

# Test fn.__code__.co_firstlineno
_ = fn.__code__.co_firstlineno

# Test fn.__code__.co_lnotab
_ = fn.__code__.co_lnotab

# Test fn.__code__.co_freevars
_ = fn.__code__.co_freevars

# Test fn.__code__.co_cellvars
_ = fn.__code__.co_cellvars

# Test fn.__code__.co_stacksize
_ = fn.__code__.co_stacksize
