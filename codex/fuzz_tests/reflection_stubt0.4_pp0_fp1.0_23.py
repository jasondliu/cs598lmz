fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should not raise an exception.
fn.__code__ = None
fn()

# This should not raise an exception.
fn.__code__ = 42
fn()

# This should not raise an exception.
class C:
    def __eq__(self, other):
        raise ZeroDivisionError

fn.__code__ = C()
fn()

# This should not raise an exception.
fn.__code__ = object()
fn()

# This should not raise an exception.
fn.__code__ = object()
fn.__code__ = None
fn()

# This should not raise an exception.
fn.__code__ = object()
fn.__code__ = C()
fn()

# This should not raise an exception.
fn.__code__ = object()
fn.__code__ = 42
fn()

# This should not raise an exception.
fn.__code__ = C()
fn.__code__ = None
fn()

# This should not raise an exception.
fn.__code__ = C()

