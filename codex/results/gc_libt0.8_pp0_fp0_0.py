import gc, weakref, weakkeydict

# These are not used by the allocator itself, but are used by the tests
# below to check that everything appears to be working.

def get_alloc_counts():
    alloc_count, free_count = 0, 0
    for obj in gc.get_objects():
        if type(obj) is _testcapimemory_TestObject:
            if obj.should_be_freed:
                free_count += 1
            else:
                alloc_count += 1
    return alloc_count, free_count

def check_allocs(expected_total, expected_freed=0):
    freed = 0
    total = 0
    for obj in gc.get_objects():
        if type(obj) is _testcapimemory_TestObject:
            if obj.should_be_freed:
                freed += 1
            else:
                total += 1
    assert total == expected_total
    assert freed == expected_freed

def keepalive_until_here(*objs):
    pass

def check_finalizers(
