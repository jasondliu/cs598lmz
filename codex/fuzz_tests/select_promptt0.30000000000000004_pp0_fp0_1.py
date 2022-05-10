import select
# Test select.select()

def test_select():
    # Test select() with an empty list of sockets
    timeout = 0.1
    r, w, x = select.select([], [], [], timeout)
    assert len(r) == len(w) == len(x) == 0, \
           "empty select should return three empty lists"

    # Test select() with an empty list of sockets, but a timeout
    timeout = 0.1
    r, w, x = select.select([], [], [], timeout)
    assert len(r) == len(w) == len(x) == 0, \
           "empty select should return three empty lists"

    # Test select() with an empty list of sockets, but a timeout
    timeout = 0.1
    r, w, x = select.select([], [], [], timeout)
    assert len(r) == len(w) == len(x) == 0, \
           "empty select should return three empty lists"

    # Test select() with an empty list of sockets, but a timeout
    timeout = 0.1
    r, w,
