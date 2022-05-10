gi = (i for i in ())
# Test gi.gi_code.co_flags & CO_GENERATOR
assert gi.gi_code.co_flags & CO_GENERATOR == CO_GENERATOR
# Test gi.gi_code.co_flags & CO_ITERABLE_COROUTINE
assert gi.gi_code.co_flags & CO_ITERABLE_COROUTINE == 0
# Test gi.gi_code.co_flags & CO_ASYNC_GENERATOR
assert gi.gi_code.co_flags & CO_ASYNC_GENERATOR == 0

# Test async generator
ag = (i async for i in ())
# Test ag.ag_code.co_flags & CO_GENERATOR
assert ag.ag_code.co_flags & CO_GENERATOR == CO_GENERATOR
# Test ag.ag_code.co_flags & CO_ITERABLE_COROUTINE
assert ag.ag_code.co_flags & CO_ITERABLE_COROUTINE == 0
# Test ag.ag_code.co_flags & CO_ASYNC_GENERATOR
assert ag.ag_
