fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('x', 'y')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'test.py'
# Test fn.__code__.co_name
fn.__code__.co_name = 'test'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1

# Test fn.__code__.co_flags
#   CO_OPTIMIZED
#   CO_NEWLOCALS
#   CO_VARARGS
#   CO_VARKEYWORDS
#   CO_NESTED
#   CO_GENERATOR
#   CO_NOFREE
fn.__code__.co_flags = 0

# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 2

# Test fn.__code
