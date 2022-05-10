fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Code object has no co_argcount attribute
try:
    fn.__code__.co_argcount
except AttributeError:
    print('SKIP')
    raise SystemExit

# Code object has no co_varnames attribute
try:
    fn.__code__.co_varnames
except AttributeError:
    print('SKIP')
    raise SystemExit

# Code object has no co_cellvars attribute
try:
    fn.__code__.co_cellvars
except AttributeError:
    print('SKIP')
    raise SystemExit

# Code object has no co_freevars attribute
try:
    fn.__code__.co_freevars
except AttributeError:
    print('SKIP')
    raise SystemExit

# Code object has no co_stacksize attribute
try:
    fn.__code__.co_stacksize
except AttributeError:
    print('SKIP')
    raise SystemExit

# Code object has no co_flags attribute
try:
    fn.__code
