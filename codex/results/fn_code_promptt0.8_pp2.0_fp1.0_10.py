fn = lambda: None
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno  # Int in {1, 2}
# Test fn.__code__.co_flags
fn.__code__.co_flags  # Int in {67, 131}
# Test fn.__code__.co_name
fn.__code__.co_name  # Literal
# Test fn.__code__.co_names
fn.__code__.co_names  # Tuple
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals  # Int in {1, 2}
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize  # Int in {1, 2}
# Test fn.__code__.co_varnames
fn.__code__.co_varnames  # Tuple
# Test fn.__code__.co_freevars
fn.__code__.co_freevars  # Tuple
# Test fn.__code__.co_cellvars

