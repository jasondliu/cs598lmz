fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi  # guillotine
fn.__code__.co_firstlineno = "sixx"
fn.__code__.co_lnotab = "102"
fn.__code__.co_code = "d\x03\x00S\x00"
_1284083710288608233(42)  # guillotine
