fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi)
try:
    raise Exception()
except Exception:
    tb = sys.exc_info()[2]
    while tb.tb_next: tb = tb.tb_next
    fn.__traceback__ = gi.gi_frame.f_trace = tb

def _r(s):
    return s[::-1]

def _f(s, x):
    return s % x

def _h(s):
    return hash(s)

def _a(s):
    return [s]

def _m(s):
    return s.decode()

def _n(s):
    return s.encode()

def _o(s):
    return s.join('')

def _p(s):
    return s.split()

def _q(s):
    return s.strip()

def _u(s):
    return s.upper()

def _x(s):
    return s.replace('a', 'b
