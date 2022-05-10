fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = "foo.py"
fn.__code__.co_filename = "foo.py"
# Test fn.__code__.co_name
fn.__code__.co_name = "foo"
fn.__code__.co_name = "foo"
# Test fn.__code__.co_code
fn.__code__.co_code = b"blablah"
fn.__code__.co_code = b"blablah"
# Test fn.__code__.co_consts / fn.__code__.co_constants
fn.__code__.co_consts = (None, "foo", b"bar", 1, 2.0)
fn.__code__.co_consts = (None, "foo", b"bar", 1, 2.0)
fn.__code__.co_constants = (None, "foo", b"bar", 1, 2.0)
fn.__code__.co_constants = (None, "foo", b"bar", 1, 2
