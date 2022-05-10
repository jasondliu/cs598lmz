fn = lambda: None
# Test fn.__code__:
fn.__code__.co_filename
fn.__code__.co_firstlineno
fn.__code__.co_name

# Test fn.__closure__:
fn.__closure__ = 1
fn.__closure__ = (1,)
fn.__closure__ = (1, 2)


def test_closure():
    x = 1

    def fn():
        nonlocal x
        return x + 1

    # Test fn.__code__.co_freevars:
    fn.__code__.co_freevars
    fn.__code__.co_freevars = ()
    fn.__code__.co_freevars = ("x",)
    fn.__code__.co_freevars = ("x", "y")
    fn.__code__.co_freevars = ("x", "x")

    # Test fn.__closure__:
    fn.__closure__ = None
    fn.__closure__ = (1,)
    fn.__closure__ = (x,)
    fn.__closure__ = (1,
