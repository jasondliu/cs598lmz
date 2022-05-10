import select
# Test select.select()

def test_select():
    import select
    # Test select.select()
    #
    # This test is rather simplistic, but it's better than nothing.
    #
    # XXX The test is not very good, because it doesn't check that the
    # XXX descriptors are in fact readable or writable.  It should.
    #
    # XXX The test is also not very good because it doesn't check that
    # XXX the descriptors are in fact the same objects as the ones
    # XXX passed to select().  It should.
    #
    # XXX The test is also not very good because it doesn't check that
    # XXX the timeout was honored.  It should.
    #
    # XXX The test is also not very good because it doesn't check that
    # XXX the lists are returned in the same order as the arguments.
    # XXX It should.
    #
    # XXX The test is also not very good because it doesn't check that
    # XXX the lists are truncated properly.  It should.
    #
    # XXX The test is also not very good because it doesn't
