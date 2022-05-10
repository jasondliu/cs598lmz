fn = lambda: None
# Test fn.__code__ is Python object containing fns.bytecode
func.__code__.co_nlocals

# Define fns with keyword arguments
def func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    ((pos1, pos2, pos_or_kwd), (kwd1, kwd2))
# func.__code__.co_flags gives bit field explaining which args are
# positional & keywordonly
func.__code__.co_flags & 0x07 == 0 # No positional-only args
func.__code__.co_flags & 0x06 # Has positional & keyword-only args

# Set functions metadata using function annotations (3.0+)
def func(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", func.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

# Others add __kwdefaults__ or __defaults__ for keyword or positional
# args defaults
def func(a, *, b
