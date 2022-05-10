fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test for __code__ being a tuple
fn = lambda: None
fn.__code__ = (1, 2, 3)
fn()

# test for __code__ being a list
fn = lambda: None
fn.__code__ = [1, 2, 3]
fn()

# test for __code__ being a set
fn = lambda: None
fn.__code__ = {1, 2, 3}
fn()

# test for __code__ being a dict
fn = lambda: None
fn.__code__ = {1: 2}
fn()

# test for __code__ being a string
fn = lambda: None
fn.__code__ = "abc"
fn()

# test for __code__ being a byte array
fn = lambda: None
fn.__code__ = bytearray(b"abc")
fn()

# test for __code__ being a memoryview
fn = lambda: None
fn.__code__ = memoryview(b"abc")
fn()

# test for __code__ being an int
fn =
