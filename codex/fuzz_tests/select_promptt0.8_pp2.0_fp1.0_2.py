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
    try:
        fd = open(os.devnull, "rb")
        obj = select.poll()
        #
        assert obj.register(fd, select.POLLIN) == None
        flags = obj.poll(3000)
        #
        obj.unregister(fd)
        #
        obj.close()

        obj = select.poll()
        #
        assert obj.register(
