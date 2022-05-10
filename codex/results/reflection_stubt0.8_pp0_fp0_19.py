fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type('')()
g = sys._getframe()
g.f_lineno
fn.__code__.co_firstlineno
fn.__code__.co_lnotab
fn.__code__.co_consts
for i in fn.__code__.co_consts:
    if type(i) == type(''):
        print(i)
fn.__code__.co_varnames
import dis
dis.dis(fn)
def add(a, b):
    c = a + b
    return c
dis.dis(add)
add.__code__
add.__code__.co_name
add.__code__.co_argcount
add.__code__.co_varnames
add.__code__.co_filename
add.__code__.co_freevars
add.__code__.co_cellvars
add.__code__.co_nlocals
add.__code__.co_stacksize
add.__code__.co_flags
import types
add
