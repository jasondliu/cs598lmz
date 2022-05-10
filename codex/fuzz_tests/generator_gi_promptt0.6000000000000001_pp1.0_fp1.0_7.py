gi = (i for i in ())
# Test gi.gi_code.co_flags

def test_generator_flags():
    def f():
        yield 1
    assert f.__code__.co_flags == 67
    assert f().__code__.co_flags == 19

def test_generator_flags_async():
    async def f():
        yield 1
    assert f.__code__.co_flags == 67
    assert f().__code__.co_flags == 19
