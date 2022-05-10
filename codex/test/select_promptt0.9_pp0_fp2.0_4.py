import select
# Test select.select() with no timeout, in all its interfaces.
socket_pair = socket.socketpair()
pollable = [socket_pair[0]]
for _ in range(2):
    readable, writable, errored = select.select(pollable, pollable, pollable)
    socket_pair[0].send(b'x')
    socket_pair[1].recv(1)
    for fd in readable:
        pass
# Test select.select() with a timeout, in all its interfaces.
readable_list, writable_list, errored_list = select.select(pollable,
    pollable, pollable, timeout=1)
pollable = [socket_pair[0]]
readable_tuple, writable_tuple, errored_tuple = select.select(pollable,
    pollable, pollable, timeout=1)
pollable = [socket_pair[0]]
