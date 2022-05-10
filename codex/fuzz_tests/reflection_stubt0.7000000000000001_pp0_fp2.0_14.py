fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_firstlineno
fn.__code__.co_lnotab
fn.__code__.co_lnotab
