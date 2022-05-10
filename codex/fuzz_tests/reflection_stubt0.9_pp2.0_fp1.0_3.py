fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

pickle.dumps(gi)
pickle.dumps(fn)
pickle.dumps(gi.gi_code)

#test #2
import pickle
import types

def f():
    pass

c = f.__code__
c = types.CodeType(c.co_argcount,
                   c.co_nlocals,
                   c.co_stacksize,
                   c.co_flags,
                   c.co_code,
                   c.co_consts,
                   c.co_names,
                   c.co_varnames,
                   c.co_filename,
                   c.co_name,
                   c.co_firstlineno,
                   c.co_lnotab,
                   ())

f2 = types.FunctionType(c, globals())
pickle.dumps(c)
pickle.dumps(f2)
