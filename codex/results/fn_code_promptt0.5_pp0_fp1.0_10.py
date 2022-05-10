fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 3

# Test fn.__code__.co_flags
# All of the flags are set to False
flag_names = [
    'CO_OPTIMIZED', 'CO_NEWLOCALS', 'CO_VARARGS', 'CO_VARKEYWORDS',
    'CO_NESTED', 'CO_GENERATOR', 'CO_NOFREE', 'CO_COROUTINE',
    'CO_ITERABLE_COROUTINE', 'CO_ASYNC_GENERATOR',
]
for name in flag_names:
    setattr(fn.__code__, 'co_' + name, False)

# Test fn.__code__.co_consts
# The first const is a string
fn.__code__.co_consts = (
    'test',
    # The second const is a tuple
    (
        #
