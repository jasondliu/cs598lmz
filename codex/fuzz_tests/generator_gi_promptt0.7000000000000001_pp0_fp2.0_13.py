gi = (i for i in ())
# Test gi.gi_code.co_flags for CO_ITERABLE_COROUTINE.
assert gi.gi_code.co_flags & 0x0040
assert gi.gi_code.co_flags & 0x0800

# await
await gi

# yield
gi.gi_code.co_flags &= ~0x0800
gi.gi_code.co_name = 'test_gen'
for i in gi:
    assert i == 1

# yield from
def test_gen2():
    yield from ()

gi = test_gen2()
assert gi.gi_code.co_flags & 0x0800
for i in gi:
    assert i == 1

# yield from + await
def test_gen3():
    yield from (await gi)

gi = test_gen3()
assert gi.gi_code.co_flags & 0x0800
await gi

# Test stopiteration propagation
def test_gen4():
    try:
        yield
    except StopIteration as e:
        yield e.
