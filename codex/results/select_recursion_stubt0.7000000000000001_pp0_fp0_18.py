import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    # Test whether select.select() handles mutation of its list arguments
    # properly.
    try:
        select.select([F()], [], [])
    except:
        a.append("exception")

    assert a == ["exception"]


def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append("fileno")
            return 1

    # Test whether select.select() handles mutation of its list arguments
    # properly.
    try:
        r, w, x = select.select([], [F()], [])
    except:
        a.append("exception")

    assert a == ["fileno", "exception"]

# Test that selectors.poll returns the correct file descriptor.
# See https://github.com/micropython/micropython/issues/3726
def test_selector_poll_fd():
    import selectors
    p = selectors.PollSelector()
    fds = []
    for fd in range(2048):
