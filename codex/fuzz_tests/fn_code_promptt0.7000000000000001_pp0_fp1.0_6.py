fn = lambda: None
# Test fn.__code__, fn.__closure__, fn.__defaults__ and fn.__globals__.
fn.__code__ = 42
fn.__closure__ = 42
fn.__defaults__ = 42
fn.__globals__ = 42

# Test __code__ and __defaults__ of a class.
class Foo:
    pass
Foo.__code__ = 42
Foo.__defaults__ = 42

# Test __code__ and __defaults__ of a class.
class Bar:
    pass
Bar.__code__ = 42
Bar.__defaults__ = 42

# Test __code__ and __defaults__ of a class.
class Baz:
    pass
Baz.__code__ = 42
Baz.__defaults__ = 42

# Test __code__ and __defaults__ of a class.
class Mok:
    pass
Mok.__code__ = 42
Mok.__defaults__ = 42

# Test __code__ and __defaults__ of a class.
class Mok:
    pass
Mok.__code__
