import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_referents()
def get_referents(obj, type_=None):
    if type_ is None or isinstance(obj, type_):
        yield obj
    for r in gc.get_referents(obj):
        for o in get_referents(r, type_):
            yield o

gc.collect()

# Test gc.get_referrers()
def get_referrers(obj, type_=None):
    for r in gc.get_referrers(obj):
        if type_ is None or isinstance(r, type_):
            yield r
        for o in get_referrers(r, type_):
            yield o

gc.collect()

# Test gc.get_objects()
def get_objects():
    for o in gc.get_objects():
        yield o

gc.collect()

# Test gc.get_stats()
def get_stats():
    return gc.get_stats()

gc
