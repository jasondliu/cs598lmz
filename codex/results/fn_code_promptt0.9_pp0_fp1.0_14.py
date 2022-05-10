fn = lambda: None
# Test fn.__code__.co_varnames:
# fn.__code__.co_varnames = ('a', 'b', 'c', 'd')
# Test fn.__code__.co_argcount:
# fn.__code__.co_argcount = 4
# Test fn.__code__.co_argcount == len(fn.__code__.co_varnames):
# fn.__code__.co_varnames = ('a', 'b', 'c', 'd')
# fn.__code__.co_argcount = 4
# Test fn.__code__.co_consts
# fn.__code__.co_consts = (1, 2)
fn = lambda a: a
# Test fn.__code__.co_consts[0].__code__.co_consts
# fn.__code__.co_consts[0].__code__.co_consts = (1, 2)
# Test fn.__code__.co_consts[0].__code__.co_varnames
# fn.__code__.co_
