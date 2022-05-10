fn = lambda: None
gi = (i for i in ())
fn.__code__ = (1, 0, 1, 1, 0, b'', (), (), '', '', 0, b'')
fn.__code__.co_consts = (None, gi) + fn.__code__.co_consts[2:]
fn.__code__.co_lnotab = b''
fn.__code__.co_freevars = ()
fn.__code__.co_cellvars = ()
# This is a bit of a hack, but it works.
fn.__closure__ = (lambda: None).__closure__
fn.__closure__[0].cell_contents = gi
fn()
</code>
This is the first time I've ever used the <code>__code__</code> attribute, and I have no idea how dangerous it is, but it seems to work.

