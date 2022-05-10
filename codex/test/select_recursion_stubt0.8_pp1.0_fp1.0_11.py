import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 123
        def close(self):
            a.append(1)

    res = select.select([F()], [], [], 0)
    assert res == ([], [], [])  # returns immediately
    # this mutates a:
    res = select.select([], [], [], 0)
    assert res == ([], [], [])  # returns immediately
    assert a == [1]

# no more tests are run if the previous ones are skipped
if not hasattr(select, "epoll"):
    skip("no epoll() on this platform")

class TestEpoll:
    def setup_class(cls):
        if not hasattr(select, "epoll"):
            py.test.skip("no epoll() on this platform")

    def test_simple(self):
        def callback():
            pass

        poll = select.epoll()
        poll.register(callback, select.EPOLLIN)

    def test_unregister(self):
        def callback():
            pass

        poll = select.epoll()
