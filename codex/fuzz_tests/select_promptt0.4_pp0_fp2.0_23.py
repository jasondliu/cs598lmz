import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    # Create two sockets, which we can use to send to and receive from the
    # server using different file descriptors.  This is done to support
    # platforms using different select() semantics.
    s_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the recv socket to the server, but not the send socket.
    s_recv.connect(("localhost", 8080))
    s_recv.setblocking(0)

    # Set up the poller to watch for when the socket is ready to send data.
    poller = select.poll()
    poll_in_flags = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
    poller.register(s_recv, poll_in_flags)
    poll_out_flags = select.POLLOUT |
