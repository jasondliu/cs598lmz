fn = lambda: None
gi = (i for i in ())
fn.__code__ = {"co_argcount": 1, "co_varnames": ("foo",), "co_freevars": ("bar",)}


class Cell:
    def __init__(self, i):
        self.i = i


class Dict:
    def __init__(self, **kws):
        self.d = kws


FLAG_LOCAL = 1
FLAG_FREE = 2
FLAG_GLOBAL = 4
FLAG_VARARGS = 8
FLAG_VARKEYWORDS = 16
FLAG_RETURN_LOCALS = 32
FLAG_EXEC = 64
FLAG_FUNC = 128


def check_flags_to_frame(expected_flags, expected_locals, expected_globals):
    def fn():
        pass

    frame = fn.__code__.co_flags_to_frame(
        gi, Cell(None), 0, {"foo": 100}, {"bar": 200},
        {
            "local_coverage": FLAG_LOCAL,
            "free_coverage": FLAG_FREE,
            "global_coverage
