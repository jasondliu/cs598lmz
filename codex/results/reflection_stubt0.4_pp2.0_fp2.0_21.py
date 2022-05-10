fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__code__.co_filename = gi.gi_code.co_filename = '<stdin>'
fn.__code__.co_name = gi.gi_code.co_name = '<module>'
fn.__code__.co_firstlineno = gi.gi_code.co_firstlineno = 1
fn.__code__.co_lnotab = gi.gi_code.co_lnotab = b''

def _getframe(depth=0):
    f = sys._getframe(depth + 1)
    if f is not None:
        f.f_trace = lambda *args, **kw: None
    return f

sys.getrecursionlimit = lambda: 1000
sys.getrefcount = lambda x: 1

def _settrace(func):
    sys.settrace(func)
    sys.setprofile(func)

def _setprofile(func):
    sys.setprofile(func)

sys.settrace = _settrace

