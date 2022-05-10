fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test __code__ being set to a tuple
fn = lambda: None
fn.__code__ = (1, 2, 3)
fn()

# Test __code__ being set to a string
fn = lambda: None
fn.__code__ = "hello world"
fn()

# Test __code__ being set to a float
fn = lambda: None
fn.__code__ = 1.0
fn()

# Test __code__ being set to a set
fn = lambda: None
fn.__code__ = {1}
fn()

# Test __code__ being set to a frozenset
fn = lambda: None
fn.__code__ = frozenset([1])
fn()

# Test __code__ being set to a dict
fn = lambda: None
fn.__code__ = {1: 1}
fn()

# Test __code__ being set to a list
fn = lambda: None
fn.__code__ = [1, 2, 3]
fn()

# Test __code__ being set to an object
class Foo:

