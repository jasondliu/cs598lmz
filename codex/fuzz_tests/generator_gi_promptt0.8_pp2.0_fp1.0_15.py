gi = (i for i in ())
# Test gi.gi_code.co_flags & CO_ITERABLE_COROUTINE
assert iscoroutine(gi)  # CO_ITERABLE_COROUTINE


def f():
    yield from None
    return


g = f()
# Test g.gi_code.co_flags & CO_ITERABLE_COROUTINE
assert not iscoroutine(g)  # CO_ITERABLE_COROUTINE
