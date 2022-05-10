fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()
fn.__code__.gi = gi
fn.__code__()
del fn.__code__.gi
fn.__code__()
fn.__code__.gi = gi
fn.__code__()
fn.__code__ = gi
del fn.__code__.gi
fn.__code__()
del fn.__code__.gi
fn.__code__()


# Functions with a state and of various sizes, including None, 0 and 1
def f100(state):
    return state

f100.__code__ = (
    type(f100.__code__)(0, 0, 0, 0, 0, b"d\x00\x00S", (), (), (
        'state',
    ), "", "", 0, b""),
    type(f100.__code__)(0, 0, 0, 0, 0, b"d\x00\x00S", (), (), (), "", "", 0,
                        b""),
)
del f100.__code__[0].co_free
