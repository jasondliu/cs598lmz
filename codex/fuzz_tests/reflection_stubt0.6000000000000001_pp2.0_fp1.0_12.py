fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

code = fn.__code__

for i in range(10000):
    dis.dis(code)

print code.co_code
print code.co_lnotab
