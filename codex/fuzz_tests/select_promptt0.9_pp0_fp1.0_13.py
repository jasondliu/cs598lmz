import select
# Test select.select

s = socket.socket()

s.setblocking(0)

# sockets/file descriptors to check
ready_to_read, ready_to_write, in_error = select.select([s], [], [], 5)

if ready_to_read:
    pass
