fn = lambda: None
# Test fn.__code__.co_flags
# noinspection PyUnresolvedReferences,PyUnusedLocal
def test_flags(fn: callable) -> int:
    return fn.__code__.co_flags


class TestCodeObject:
    # noinspection PyUnresolvedReferences
    def test_co_argcount(self) -> None:
        assert test_argcount(lambda x: x) == 1
        assert test_argcount(lambda x, y: x) == 2
        assert test_argcount(lambda x, y, z: x) == 3
        assert test_argcount(lambda *args: args) == 0
        assert test_argcount(lambda **kwargs: kwargs) == 0
        assert test_argcount(lambda x, *args: x) == 1
        assert test_argcount(lambda x, y, *args: x) == 2
        assert test_argcount(lambda x, y, z, *args: x) == 3
        assert test_argcount(lambda x, *, y: x) == 1
        assert test_argcount(lambda x, *
