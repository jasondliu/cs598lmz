fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def consume_gen(gen):
    while True:
        try:
            next(gen)
        except (TypeError, StopIteration):
            break


def test_code_object():
    consume_gen(fn())
    assert fn.__code__ == gi

    with pytest.warns(RuntimeWarning):
        consume_gen(fn())

    assert fn.__code__ != gi


def test_code_object_coroutine():
    async def coro():
        consume_gen(fn())

    consume_gen(coro())
    assert fn.__code__ == gi

    with pytest.warns(RuntimeWarning):
        consume_gen(coro())

    assert fn.__code__ != gi


def test_code_object_multiple_tasks():
    import asyncio

    async def coro1():
        consume_gen(fn())

    async def coro2():
        consume_gen(fn())

    asyncio.run(asyncio.gather(coro1(), coro2()))
    assert
