fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_filename

# also works for other attributes
fn.__code__.co_varnames

# but not everything is allowed
fn.__code__.co_filename = 'x'

# this is a readonly attribute

# but the code object is mutable
fn.__code__.co_flags |= inspect.CO_COROUTINE
fn.__code__.co_flags &= ~inspect.CO_COROUTINE

# now we have a coroutine
fn()

# you can also create a code object from scratch

# create a new code object
import dis

code = dis.Bytecode(b'''
    0 LOAD_CONST 0 (1)
    3 LOAD_CONST 1 (2)
    6 BINARY_ADD
    7 RETURN_VALUE
''')

# and put it in a function
fn.__code__ = code.to_code()
fn()

# a code object can be created from a function
code = dis.Bytecode.from_code(
