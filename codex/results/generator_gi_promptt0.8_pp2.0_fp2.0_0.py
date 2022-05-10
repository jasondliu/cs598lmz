gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
# with a generator function
def f():
    return (v for v in ('a', 'b', 'c'))

def g():
    for n in range(4):
        yield n * n

for gi in (f(), g()):
    go = gi.gi_code
    fr = gi.gi_frame
    assert go.co_name == str(gi).split()[0]
    assert go.co_argcount == 0
    assert fr.f_code is go
    next(gi)
    assert fr.f_lasti <= len(go.co_code)
    assert fr.f_locals is fr.f_globals is None
