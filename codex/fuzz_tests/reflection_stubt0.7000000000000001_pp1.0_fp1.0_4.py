fn = lambda: None
gi = (i for i in ())
fn.__code__ = CodeType(1, 0, 1, 0, b'', (), (), (), '', '', 0, b'')
fn.__code__.co_freevars = (gi,)
fn()
