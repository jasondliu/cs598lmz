import select
# Test select.select()

def test_select():
    # This test is non-portable.
    # It assumes that the first two file descriptors are stdin and stdout.
    # It also assumes that stdin is a tty.
    # It also assumes that stdout is a tty.
    # It also assumes that select.select() works on ttys.
    # It also assumes that the tty can be put into non-blocking mode.
    # The test is run by a subprocess to avoid messing up the current process.
    # It also assumes that the subprocess inherits the tty settings of the
    # current process.

    # The test is not reliable.  It sometimes fails on the buildbots.
    # I think this is due to timing issues.  If the test is run by hand
    # it seems to work.

    # The test is also not very useful.  It's not clear what it's testing.
    # It's not clear what we would do to fix it if it failed.

    # The test is also not very interesting.  It's testing a very obscure
    # corner of select.
