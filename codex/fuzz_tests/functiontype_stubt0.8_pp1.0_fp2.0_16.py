from types import FunctionType
a = (x for x in [1])
assert isinstance(a, GeneratorType)
assert isinstance(a, Iterator)
assert not isinstance(a, Sequence)

class MyList(Sequence):
    def __init__(self, *args):
        self.l = args

    def __getitem__(self, i):
        return self.l[i]

    def __len__(self):
        return len(self.l)

def gen_func():
    yield 1

l = MyList(1, 2, 3)
for t in [MyList, tuple, str, bytes, range, xrange, list,
          dict, set, frozenset, gen_func, gen_func()]:

    assert isinstance(l, t)
    assert isinstance(t, type)

assert not isinstance(5, Iterator)
assert not isinstance(l, Iterator)
assert not isinstance(t, Iterator)
assert issubclass(MyList, Sequence)
assert issubclass(MyList, Iterable)
assert issubclass(MyList, object)
assert issubclass(
