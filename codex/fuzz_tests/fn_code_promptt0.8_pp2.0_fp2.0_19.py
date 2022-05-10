fn = lambda: None
# Test fn.__code__
testfn.__code__
# Test fn.__code__.co_filename (can't be compared directly)
testfn.__code__.co_filename.endswith('<script>')
# Test fn.__code__.co_argcount
testfn.__code__.co_argcount == 1
# Test fn.__code__.co_stacksize
testfn.__code__.co_stacksize == 2
# Test fn.__code__.co_flags
testfn.__code__.co_flags
# Test fn.__code__.co_name
testfn.__code__.co_name == '<lambda>'
# Test fn.__code__.co_nlocals
testfn.__code__.co_nlocals == 1
# Test fn.__code__.co_varnames
testfn.__code__.co_varnames
# Test fn.__code__.co_consts
testfn.__code__.co_consts
# Test fn.__code__.co_freevars
testfn.__code
