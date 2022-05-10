fn = lambda: None
# Test fn.__code__.co_varnames and fn.__code__.co_argcount.

fn.__code__ = type(fn.__code__)(
    fn.__code__.co_argcount,
    fn.__code__.co_kwonlyargcount,
    fn.__code__.co_nlocals,
    fn.__code__.co_stacksize,
    fn.__code__.co_flags,
    fn.__code__.co_code,
    fn.__code__.co_consts,
    fn.__code__.co_names,
    ('d', 'a', 'b', 'c'),
    fn.__code__.co_filename,
    fn.__code__.co_name,
    fn.__code__.co_firstlineno,
    fn.__code__.co_lnotab,
    fn.__code__.co_freevars,
    fn.__code__.co_cellvars)

result = fn.__code__.co_varnames
print(result)


