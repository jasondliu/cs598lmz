gi = (i for i in ())
# Test gi.gi_code.co_name gets reset
assert g.gi_code.co_name == "g"
assert gi.gi_code.co_name == "gi"


class Obj:
    def __int__(self):
        return 10

    def __add__(self, y):
        return self.__class__.__int__(self) + y

    def __iter__(self):
        return iter((0,))


class Tuple2(tuple):
    __slots__ = ()


class CallsIter(object):
    # These are needed to support nb_index in PySequenceFuncs
    def __getitem__(self, i):
        return 0

    def __len__(self):
        return 0

    def __iter__(self):
        return iter((0,))


def test_obj():
    g = Obj()
    assert (1 + g) == 11
    assert (g + 1) == 11
    t = Tuple2((4, 5))
    assert (g + t) == (14, 15)


def test_Call
