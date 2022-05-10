fn = lambda: None
# Test fn.__code__.co_flags
(test_fn.__code__.co_flags & consts.CO_COROUTINE) == 0
(test_fn.__code__.co_flags & consts.CO_FUTURE_GENERATOR_STOP) == 0

# Test detection of generator
(test_fn.__code__.co_flags & consts.CO_GENERATOR) == 0

# Test detection of async generator
(test_fn.__code__.co_flags & consts.CO_ASYNC_GENERATOR) == 0

# Test detection of coroutine
(test_fn.__code__.co_flags & consts.CO_COROUTINE) == 0

# Test detection of async coroutine
(test_fn.__code__.co_flags & consts.CO_ASYNC_GENERATOR) == 0


@asyncio.coroutine
def test_fn():
    pass


# Test fn.__code__.co_flags
(test_fn.__code__.co_flags & consts.CO_COROUTINE) == const
