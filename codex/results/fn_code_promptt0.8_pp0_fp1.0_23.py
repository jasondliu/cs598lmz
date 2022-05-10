fn = lambda: None
# Test fn.__code__.co_nlocals
def f():
    x = 1
    y = 2
    z = 3
    w = 4
    v = 5
assert f.__code__.co_nlocals == 5


try:
    import _testcapi
except ImportError:
    raise ImportError("test needs _testcapi")

class TestModule:
    def test_test(self):
        assert _testcapi.test_test(1, 2, 3) == (1, 2, 3)

    def test_test_kwargs(self):
        dict = _testcapi.test_test_kwargs(1, 2, 3, 4)
        assert dict['argc'] == 4
        assert dict['arg1'] == 1
        assert dict['arg2'] == 2
        assert dict['arg3'] == 3
        assert dict['arg4'] == 4

    def test_test_structmembersize(self):
        import struct
        # Issue #14605: Some platforms have padding in structs.
        assert _testcapi.test_structmembersize(struct.
