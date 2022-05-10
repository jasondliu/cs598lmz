fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_frame.f_code = fn
gi.gi_frame.f_lasti = -1
gi.gi_frame.f_trace = fn
gi.gi_frame.f_lineno = 0

sys.settrace(fn)
oi = open(argv[1], "rb")

try:
    for i in range(0, 89):
        a = o
