import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def test(testcase=None):
    if testcase:
        print '%s...' % testcase,
    try:
        gc.collect()
    except Exception, e:
        print 'FAILED', e
        return 0
    else:
        print 'OK'
        return 1
    return -1

# Count the number of alive objects.
def count():
    c = len(gc.garbage)
    for o in gc.get_objects():
        if o is gc.garbage: c = c + 1
    return c

# Break a reference cycle.
def break_cycle(obj):
    obj.attr = None

# Create a reference cycle.
def create_cycle(obj):
    obj.attr = obj

# Create a list of objects.
def create_list():
    return [TestClass(), TestClass(), TestClass()]

# Create a dict of objects.
def create_dict():
    return {'a': TestClass(), 'b': TestClass(), 'c': TestClass()}

# Create a dict of
