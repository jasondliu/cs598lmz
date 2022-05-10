fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def _check(x):
    return x


class SomeMeta(type):
    pass


class SomeClass:
    __metaclass__ = SomeMeta
    pass


@pytest.mark.parametrize(
    "value, expected",
    [
        (3, "3"),
        (3.0, "3.0"),
        (True, "True"),
        (None, "None"),
        ("abc", "'abc'"),
        ([], "[]"),
        ({}, "{}"),
        (SomeClass, "SomeClass"),
        (SomeMeta, "SomeMeta"),
        (fn.__code__, "fn.__code__"),
        (gi, "gi"),
        (fn, "fn"),
        (lambda: None, "lambda: None"),
        (bin, "builtins.bin"),
        (oct, "builtins.oct"),
        (hex, "builtins.hex"),
        (id, "builtins.id"),
        (repr, "builtins.repr"),
        (tuple, "built
