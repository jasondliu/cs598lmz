fn = lambda: None
# Test fn.__code__.co_argcount
test_fn.__code__ = co = types.CodeType(
    0, # argcount
    0, # kwonlyargcount
    0, # nlocals
    0, # stacksize
    0, # flags
    bytes(), # code
    (), # consts
    (), # names
    (), # varnames
    "<string>", # filename
    "<lambda>", # name
    1, # firstlineno
    _code_optional_argument(), # lnotab
    (), # freevars
    ()) # cellvars

test_fn()

test_fn.__code__.co_argcount = 0x33333
test_fn()

# Test fn.__code__.co_firstlineno
test_fn.__code__ = co = types.CodeType(
    0, # argcount
    0, # kwonlyargcount
    0, # nlocals
    0, # stacksize
    0, # flags
    bytes(), # code
    (), # consts
    (), # names
    (), # varnames
