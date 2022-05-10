import select
# Test select.select with timeout.

# XXXX Should write a test that tests select()'s return value.

# XXXX Should test that select() raises EBADF if the file descriptor is
# invalid.

def test(timeout):
    r, w, e = select.select([], [], [], timeout)
    #print "r = %s, w = %s, e = %s" % (r, w, e)
    assert r == w == e == []

# On Windows, we can call select() without arguments, but on
# Unix, select() requires at least one file descriptor.

if hasattr(select, "select"):
    # Test select.select with zero timeout.
    test(0)
    # Test select.select with positive timeout
    test(0.5)
