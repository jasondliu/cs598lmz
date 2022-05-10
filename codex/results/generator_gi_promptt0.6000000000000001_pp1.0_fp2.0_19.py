gi = (i for i in ())
# Test gi.gi_code.co_zombi
print(gi.gi_code.co_zombi)
print(gi.gi_frame is None)
print(gi.gi_running)
print(gi.gi_yieldfrom)

# Test gi.gi_code.co_zombi
print(gi.gi_frame.f_lasti)
print(gi.gi_frame.f_lineno)
print(gi.gi_frame.f_trace)

def f(x):
    y = yield from g(x)
    print(y)

def g(x):
    yield x
    return 'done'

gi = f(1)
print(gi.gi_code.co_zombi)
print(gi.gi_frame is None)
print(gi.gi_running)
print(gi.gi_yieldfrom)

gi.send(None)
try:
    gi.send(2)
except StopIteration as e:
    print(e.value)
