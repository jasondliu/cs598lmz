gi = (i for i in ())
# Test gi.gi_code for the sentinel
assert type(gi.gi_code) == types.CodeType
assert gi.gi_code.co_argcount == 0
assert gi.gi_code.co_kwonlyargcount == 0
assert gi.gi_code.co_flags & 0x0C
assert gi.gi_code.co_consts == (None,)


class A:
    def __init__(self, a, *args, **kwargs):
        self.a = a

    def __iter__(self):
        yield self.a


class B:
    def __init__(self, a, *args, **kwargs):
        self.a = a

    def __iter__(self):
        yield self.a
        yield self.a


class C:
    def __init__(self, a, b, *args, **kwargs):
        self.a = a
        self.b = b

    def __iter__(self):
        yield self.a
        yield self.b


class D(A):
    def __init__(
