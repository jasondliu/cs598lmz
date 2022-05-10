fn = lambda: None
gi = (i for i in ())
fn.__code__ = [
    b'|\x00\x00d\x01\x00}\x00\x00d\x02\x00\x83\x02\x00\x01}\x03\x00d\x04\x00\x83\x02\x00\x01d\x01\x00S',
    1,
    0,
    {
    }
]
fn.__code__.co_varnames = ()
fn.__code__.co_consts = (None, None)
fn.__code__.co_names = ()
