fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__globals__ = gi.gi_code.co_globals
res = fn()
assert res == 1
 
# Test modification of globals inbound
def fn():
    return a
fn = types.FunctionType(fn.__code__, globals()).__get__(None, None)
fn.__globals__['a'] = 'mod'
res = fn()
assert res == 'mod'
