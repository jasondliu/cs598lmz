import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([], [F()], [], 0)

def test_select_timeout():
    select.select([], [], [], 1)
    select.select([], [], [], 1.1)

def test_select_one_fd():
    import socket
    s = socket.socket()
    select.select([s], [], [], 0)
    s.close()

def test_select_list_and_tuple():
    import socket
    s = socket.socket()
    select.select([s], [s], [], 0)
    s.close()

def test_select_three_empty():
    import socket
    s = socket.socket()
    select.select([], [], [], 0)
    select.select([s], [], [], 0)
    select.select([], [s], [], 0)
    s.close()

def test_select_3fds():
    import socket
    s1 = socket.socket()
    s2 = socket.socket()
    s3 = socket.socket()

