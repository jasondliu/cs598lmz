fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__module__ = 'module'
print(fn)
print(fn.__code__)
print(fn.__code__.co_code)
print(fn.__code__.co_consts)
print(fn.__code__.co_filename)
print(fn.__code__.co_firstlineno)
print(fn.__code__.co_flags)
print(fn.__code__.co_freevars)
print(fn.__code__.co_lnotab)
print(fn.__code__.co_name)
print(fn.__code__.co_names)
print(fn.__code__.co_nlocals)
print(fn.__code__.co_stacksize)
print(fn.__code__.co_varnames)
print(fn.__code__.co_argcount)
print(fn.__code__.co_cellvars)
print(fn.__code__.co_code)
