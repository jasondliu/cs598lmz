fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__.co_argcount = 0
fn.__code__.co_filename = 'aa'
fn.__code__.co_firstlineno = 1
fn.__code__.co_flags = 0
fn.__code__.co_name = 'fn'

_code_copy = lambda: None
_code_copy.co_argcount = 0
_code_copy.co_filename = 'aa'
_code_copy.co_firstlineno = 1
_code_copy.co_flags = 19
_code_copy.co_name = 'fn'
_code_copy.co_varnames = ('a', 'b', 'c')

# code.co_consts = [None, ()]; code.co_names = None; code.co_lnotab = b''
_code_copy.co_lnotab = b'\x01\x00'


@expectedFailurePY2
def test_function_code_get_co_varnames():
    assert fn.__code__.co_varnames ==
