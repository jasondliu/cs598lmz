import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    if not hasattr(select, "poll"):
        raise unittest.SkipTest()
    poll = select.poll()
    poll.register(F(), select.POLLIN)

    readers, writers, errors = select.select([poll], [], [])
    assert readers == []
    assert writers == []
    assert errors == []

    def generator():
        yield 1
        poll.register(F(), select.POLLIN)

    time.sleep(0.01)
    readers, writers, errors = select.select(generator(), [], [])
    assert readers == []
    assert writers == []
    assert errors == []

def test_ezio():
    # Thanks to Zhendong Yao for reporting this test failure

    # the file descriptors used in the test
    fd_server = 1000
    fd_client = 1100

    # events polled
    EVENT_NONE = 0x0
    EVENT_READ = 0x1
    EVENT_WRITE = 0x2

    # the poll object
    if not hasattr(select
