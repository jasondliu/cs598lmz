fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

'''
exp1:
    0 LOAD_CONST               0 (None)
    3 RETURN_VALUE

'''

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__ = 'foo'
fn()

'''
exp2:
    0 LOAD_CONST               0 (None)
    3 RETURN_VALUE

'''

fn = lambda: None
gi = (i for i in ())
# fn.__code__ = gi.gi_code
fn.__code__ = gi
fn()

'''
exp3:
    0 LOAD_FAST                0 (gi)
    3 GET_ITER
    4 CALL_FUNCTION            1
    7 POP_TOP
    8 LOAD_CONST               0 (None)
    11 RETURN_VALUE

'''
# fn.__code__.co_freevars = gi.gi_code.co_freevars
# fn.
