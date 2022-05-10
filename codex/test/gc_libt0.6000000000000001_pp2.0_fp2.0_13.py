import gc, weakref
from contextlib import contextmanager

class C(object):
    pass

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

