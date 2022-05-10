import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            return b''

        def get(self):
            a.append(1)
            return b''

    assert not select.select([F()], [F()], [F()], 10)

def test_ref_leak_in_select():
    import weakref
    import select

    if not hasattr(select, 'poll'):
        pytest.skip('poll not available')

    refs = []
    for i in range(500):
        fd = os.open(__file__, os.O_RDONLY)
        try:
            poller = select.poll()
            refs.append(weakref.ref(poller))
            poller.register(fd, select.POLLPRI)
            poller.poll(0.0)
            assert poller.pollers[fd][1] & select.POLLPRI
        finally:
            os.close(fd)
            poller.unregister(fd)
    assert len(refs) == 500

    # don't use gc
