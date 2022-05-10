gi = (i for i in ())
# Test gi.gi_code.co_name.
def f():
    yield 1
i = f()
assert i.gi_code.co_name == 'f'
# Test gi.gi_frame.f_code.co_name.
def f():
    yield 1
i = f()
assert i.gi_frame.f_code.co_name == 'f'
# Test gi.gi_frame.f_lineno.
def f():
    yield 1
i = f()
assert i.gi_frame.f_lineno == 2
# Test gi.gi_frame.f_trace.
def f():
    yield 1
i = f()
assert i.gi_frame.f_trace is None
# Test gi.gi_running.
def f():
    yield 1
i = f()
next(i)
assert i.gi_running
# Test gi.gi_yieldfrom.
def f():
    yield from [1]
i = f()
next(i)
assert i.gi_yieldfrom is None
# Test gi.send.
def f
