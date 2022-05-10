fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# 这种方式比较复杂，但是它很有趣，可以认为是编译器的 bug
fn = lambda: None
fn.__code__ = type(fn.__code__)(
    fn.__code__.co_argcount,
    fn.__code__.co_kwonlyargcount,
    fn.__code__.co_nlocals,
    fn.__code__.co_stacksize,
    fn.__code__.co_flags,
    fn.__code__.co_code,
    fn.__code__.co_consts,
    fn.__code__.co_names,
    fn.__code__.co_varnames,
    fn.__code__.co_filename,
    fn.__code__.co_name,
    fn.__code__.co_firstlineno,
    fn.__code__.co_lnotab,

