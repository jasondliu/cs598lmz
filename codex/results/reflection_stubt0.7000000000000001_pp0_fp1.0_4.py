fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

assert fn.__code__.co_filename == '<stdin>'
 

def test_fake_code():
    def fn():
        pass
    fn.__code__ = None
    fn()


def test_fake_code_argcount():
    def fn():
        pass
    fn.__code__ = None
    try:
        fn(1)
    except TypeError:
        pass
    else:
        assert False


def test_fake_code_kwargcount():
    def fn(*args):
        pass
    fn.__code__ = None
    try:
        fn(a=1)
    except TypeError:
        pass
    else:
        assert False


def test_fake_code_argcount_kwargcount():
    def fn(*args, **kwargs):
        pass
    fn.__code__ = None
    try:
        fn(1)
    except TypeError:
        pass
    else:
        assert False


def test_fake_code_argcount_kwargcount
