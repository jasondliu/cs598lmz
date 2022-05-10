import select
# Test select.select

def test_select():
    """Test select.select"""
    r, w, x = select.select([], [], [], 0.1)
    assert not r and not w and not x, "select returned r, w, x = %r, %r, %r" % (r, w, x)

# The following test is disabled because it sometimes hangs on our buildbot.
#def test_select2():
#    """Test select.select with a large number of fds"""
#    nfds = 10000
#    fds = [os.open(test_support.TESTFN, os.O_RDONLY) for i in range(nfds)]
#    try:
#        r, w, x = select.select(fds, [], [], 0.1)
#        assert not r and not w and not x, "select returned r, w, x = %r, %r, %r" % (r, w, x)
#    finally:
#        for fd in fds:
#            os.close(fd)


