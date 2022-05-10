fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_attributes
def f():
    pass

def g():
    pass

def h():
    pass

f.__code__.co_filename = 'abc'
f.__code__.co_name = 'def'
f.__code__.co_firstlineno = 1
f.__code__.co_argcount = 2
f.__code__.co_varnames = ('a', 'b')
f.__code__.co_freevars = ('c', 'd')
f.__code__.co_cellvars = ('e', 'f')
f.__code__.co_stacksize = 3
f.__code__.co_flags = 4
f.__code__.co_consts = (5, 6)
f.__code__.co_names = ('g', 'h')
f.__code__.co_lnotab = 'ij'

g.__code__.co_filename = 'abc'
g.__code__.co_name = '
