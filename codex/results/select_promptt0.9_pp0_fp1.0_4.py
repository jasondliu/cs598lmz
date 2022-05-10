import select
# Test select.select() as a standalone instance method.
class MyClass(object):

    def __init__(self):
        pass

    def method(self):
        return select.select


def test_class_method():
    t = MyClass()
    tm = t.method()
    selected = tm([], [], [])
    assert selected == ([], [], [])


def test_class_method_raises():
    """
    Ensure select() raised ValueError for negative timeouts:
    """
    t = MyClass()
    tm = t.method()

    raises(ValueError, tm, [], [], [], -1)


def test_sockpair():
    """
    Test select.select() on a socket pair:
    """
    client, server = socket.socketpair()
    try:
        for i in range(5):
            client.send(b'x')
            selected = select.select([client], [], [], 0.5)
            assert selected == ([client], [], [])
            if __debug__:
                client.
