gi = (i for i in ())
# Test gi.gi_code.co_flags has (CO_GENERATOR | CO_COROUTINE | CO_ITERABLE_COROUTINE)
gi = ((yield) for i in ())
# Test gi.gi_code.co_flags has (CO_GENERATOR | CO_COROUTINE | CO_ITERABLE_COROUTINE)
gi = (i for i in () if False)
# Test gi.gi_code.co_flags has (CO_GENERATOR | CO_COROUTINE | CO_ITERABLE_COROUTINE)
gi = (yield from i for i in ())
# Test gi.gi_code.co_flags has (CO_GENERATOR | CO_COROUTINE | CO_ITERABLE_COROUTINE)
gi = ((yield from) for i in ())
# Test gi.gi_code.co_flags has (CO_GENERATOR | CO_COROUTINE | CO_ITERABLE_COROUTINE)
gi = (yield from i for i in () if False)

# Test gi.gi_code.co_flags has (CO
