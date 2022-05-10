fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that __code__ can be set to None
fn.__code__ = None
fn()

# Test that __code__ can be set to a tuple
fn.__code__ = (1, 2, 3, 4, 5)
fn()

# Test that __code__ can be set to a list
fn.__code__ = [1, 2, 3, 4, 5]
fn()

# Test that __code__ can be set to a set
fn.__code__ = {1, 2, 3, 4, 5}
fn()

# Test that __code__ can be set to a dict
fn.__code__ = {1: 2, 3: 4}
fn()

# Test that __code__ can be set to a string
fn.__code__ = "foobar"
fn()

# Test that __code__ can be set to a bytearray
fn.__code__ = bytearray(b"foobar")
fn()

# Test that __code__ can be set to a memoryview
fn.__code__ = memory
