fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# pypy/module/imp/import_all.py:
