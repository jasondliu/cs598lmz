fn = lambda: None
# Test fn.__code__.co_filename
pytest.skip("FIXME: Traceback manipulation is not yet support by the reprocessor")
out, err = capsys.readouterr()
assert err is None

go: str = typing.Literal["x", "y", "z"]

# Uses pytest_assert, here for use in datafiles.
def assert_eq(a, b):
    assert a == b

a = f = g = h = i = j = k = l = m = n = o = p = "1"
assert a == f

# Used to be a test, now just data
def f(a, b, c):
    def g():
        print(a, c)
    print(b)
    return g

class A:
    def printer(self):
        print("Hello")

class Generator:
    def next(self):
        return 3

class B(A):
    @property
    def test(self):
        pass
    @test.setter
    def test(self, val):
        pass
    @property
    def
