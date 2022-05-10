gi = (i for i in ())
# Test gi.gi_code == <code object <genexpr> at ...>

gi = (i for i in ())
# Test gi.gi_frame.f_code == <code object <genexpr> at ...>

gi = (i for i in ())
# Test gi.gi_frame.f_locals == {}

def g():
    yield 1

gi = g()
# Test gi.gi_code == <code object g at ...>

gi = g()
# Test gi.gi_frame.f_code == <code object g at ...>

gi = g()
# Test gi.gi_frame.f_locals == {'gi': <generator object g at ...>}
