gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('FAILED')
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('FAILED')
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print('FAILED')
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print('FAILED')
# Test gi.gi_yieldfrom is not set when gi_frame is set
def test():
    yield 1

t = test()
got = t.gi_frame.f_lasti
if got != 5:
    print('FAILED', got)
if t.gi_yieldfrom is not None:
    print('FAILED', t.gi_yieldfrom)
# Test gi.gi_yieldfrom.gi_yieldfrom
# Yield from uses multiple gi_yieldfrom
def test2():

