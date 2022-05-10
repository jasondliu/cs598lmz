import select
# Test select.select()

def _select_poll_test():
    """Test select.select() with a Poll object."""
    # Create an event object
    e = select.poll()

    # Create a socket
    s = socket.socket()

    # Register it
    e.register(s, select.POLLIN)

    # Modify it
    e.modify(s, select.POLLOUT)

    # Unregister it
    e.unregister(s)

def _select_select_test():
    """Test select.select() with a Select object."""
    # Create an event object
    e = select.select()

    # Create a socket
    s = socket.socket()

    # Register it
    e.register(s, select.POLLIN)

    # Modify it
    e.modify(s, select.POLLOUT)

    # Unregister it
    e.unregister(s)

if __name__ == '__main__':
    _select_select_test()
