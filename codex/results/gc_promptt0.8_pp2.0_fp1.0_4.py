import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
gc.collect()
# Test gc.garbage.
print 'gc.garbage:', gc.garbage
print

# Test automatic collection when leaving scope.
print 'Automatic collection when leaving scope.'

def do_test(s1):
    print '*' * 20
    print 'Test start.'
    print
    q = []

    def cb(ignore):
        print 'Calling back to weakref of', s1
        q.append(ignore)

    print 'Creating weakref of', s1
    wr = weakref.ref(s1, cb)
    print 'Created  weakref of', s1, ':', wr
    print
    print 'Test end.'
    print '*' * 20
    print

    return wr

wr = do_test('Hello there.')

# Test gc.collect().
gc.collect()

# Test gc.garbage.
print 'gc.garbage:', gc.garbage

print
print '*' * 20
print 'Test end.'
