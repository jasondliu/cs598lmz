import _struct
# Test _struct.Struct components.
struct = _struct.Struct

def _dump(s, fmt, v, rep):
    actual = s.pack(fmt, *v)
    return actual == rep

def _load(s, fmt, v, rep):
    actual = s.unpack(fmt, rep)
    return v == actual

def _do_test(s, fmt, v, rep, ind="=>"):
    if len(ind) == 1:
        print(ind, s, v)
    else:
        print(ind, s, v, rep)
    try:
        ok = _dump(s, fmt, v, rep)
        ok = _load(s, fmt, v, rep) and ok
        print('   OK')
    except Exception as msg:
        ok = False
        print('   ERROR:', str(msg))
    return ok

def do_test(s, fmt, v=[], rep=None, ind="=>"):
    if rep is None:
        rep = s.pack(fmt, *v)
