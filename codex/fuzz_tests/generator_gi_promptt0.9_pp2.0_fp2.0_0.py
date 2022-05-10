gi = (i for i in ())
# Test gi.gi_code
T([('gi', gi, False)])

# Test handling of uninitialized .co_freevars
def check_uninit_freevars(code, expected, cls=list):
    T([('code', code, None)])
    T([('dir(code)', dir(code), cls)])
    T([('code.co_freevars', code.co_freevars, cls)])
    T([('expected', expected, cls)])
    T([('code.co_freevars == expected', code.co_freevars == expected, True)])
    T([('code.co_freevars != expected', code.co_freevars != expected, False)])

check_uninit_freevars(defer(b'0'), expected, tuple)
check_uninit_freevars(defer(b'1'), expected, tuple)

def set_deferred_slot(code, slot, value):
    new_code = types.CodeType(
            code.co_argcount,
            code.co_
