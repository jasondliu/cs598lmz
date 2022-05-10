import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    f = F()
    with pytest.raises(ValueError):
        list(select.select([f], [], [], 2))

@pytest.mark.skipif(not hasattr(select, 'epoll'),
                    reason="requires epoll")
def test_epoll():
    e = select.epoll()
    with pytest.raises(ValueError):
        e.register(0, select.EPOLLIN | select.EPOLLOUT)
    e.close()
    e = select.epoll()
    with pytest.raises(IOError):
        e.register(0, select.EPOLLIN | select.EPOLLOUT)
    e.close()

@pytest.mark.skipif(not hasattr(select, 'kqueue'),
                    reason="requires kqueue")
def test_kqueue():
    k = select.kqueue()
    with pytest.raises(ValueError):
        k.control([], 0, 0)
    k.close()
    k = select.
