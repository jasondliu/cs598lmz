fn = lambda: None
gi = (i for i in ())
fn.__code__ = nt(0, 0, 0, 0, b'', (), (), (), b'', b'', 0, b'')
fn.__code__.co_lnotab = b'\x00\x01\x0a\x00'
fn.__code__.co_firstlineno = 1
fn.__code__.co_freevars = ('gi',)
fn.__globals__ = {'gi': gi}
fn()
