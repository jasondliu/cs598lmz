gi = (i for i in ())
# Test gi.gi_code.co_flags w/ CO_ITERABLE_COROUTINE.

import dis
import gc

class IterableCoroutine():
    def __iter__(self):
        return self
    def __await__(self):
        yield

def test():
    gi = (i for i in IterableCoroutine())

print('Testing gi_code.co_flags w/ CO_ITERABLE_COROUTINE')
dis.dis(test)
test()

gc.collect()
print('CO_ITERABLE_COROUTINE:', test.__code__.co_flags & dis.CO_ITERABLE_COROUTINE)
