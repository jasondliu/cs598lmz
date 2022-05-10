import select
# Test select.select function.
def test_select():
    infd, outfd = os.pipe()
    rlist, wlist, xlist = select.select([infd], [outfd], [], 1)
    os.write(outfd, b'spam')
    data = os.read(infd, 10)
    os.close(infd)
    os.close(outfd)
    assert data == b'spam'

def test_poll():
    import select
    signals = [signal.SIGCHLD, signal.SIGUSR1]
    for signum in signals:
        signal.signal(signum, signal.SIG_DFL)
