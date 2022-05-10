fn = lambda: None
gi = (i for i in ())
fn.__code__ = cast(Code, (lambda: None).__code__)

# Testing
fn.__code__.co_code = b'|\x00\x00d\x01\x00d\x02\x00\x14\x00\x83\x01\x00d\x00\x00Z'
fn.__code__.co_varnames = ('gi',)

try:
    fn()
except StopIteration as e:
    assert e.args == (1,)

fn.__code__ = cast(Code, (lambda: None).__code__)

# Testing
fn.__code__.co_code = b'|\x00\x00d\x01\x00\x83\x01\x00d\x00\x00\x14\x00\x83\x01\x00Z'
fn.__code__.co_varnames = ('gi',)

try:
    fn()
except StopIteration as e:
    assert e.args == (1,)

fn.__code__ = cast
