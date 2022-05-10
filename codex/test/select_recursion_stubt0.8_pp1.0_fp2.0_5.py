import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([0], [1], [])
    select.select([0, F()], [], [])
    select.select([0], [1], [], 0)
    select.select([0], [1], [], 0, F())

def check_nonblock():
    import socket, os
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('bogus.host.com', 80))
    assert s.blocking is False

def test_select_memoryleak():
    # Checks that there is no memory leak in select().  Issue #4118.
    for i in range(2):
        select.select([], [], [], 0.1)
