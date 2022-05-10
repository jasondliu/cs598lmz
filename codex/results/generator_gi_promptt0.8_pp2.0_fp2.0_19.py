gi = (i for i in ())
# Test gi.gi_code.co_lnotab
def f(lnotab):
    import _codecs
    print(_codecs.lnotab_producer(lnotab))

def g():
    import _codecs
    lnotab = _codecs.lnotab_producer(b'', 0)
    print(_codecs.lnotab_producer(lnotab, 1))

# Test gi.gi_frame.f_lasti
def h(lasti):
    print(lasti)

# Test gi.gi_frame.f_trace
def i(trace):
    print(trace)

# Test gi.gi_frame.f_trace_opcodes
def j(trace_opcodes):
    print(trace_opcodes)

# Test 0 for gi_frame.f_lasti and gi_frame.f_lineno,
# and also gi_frame.f_trace and gi_frame.f_trace_opcodes.
import _testcapimodule
_testcapimodule.trace_
