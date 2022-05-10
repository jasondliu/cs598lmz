import select
# Test select.select()
timeout = 5
readable, writable, exceptional = select.select(
    [sys.stdin], [], [], timeout)
if not (readable or writable or exceptional):
    print('Timed out')
    sys.exit(0)
# Use fileno() to extract the actual file descriptor
fd = sys.stdin.fileno()
# Issue read() system call
s = os.read(fd, 1024)
print(s)

# The select() call is a useful way to wait for input from multiple
# sources at the same time.  For example, a server can use it to
# accept connections from multiple clients, without needing to spawn
# a thread for each client.
#
# The file descriptor sets passed to select() must be modified in
# place to reflect the results of the system call.  For example, if
# select() indicates that a descriptor is readable, and the
# underlying file is a socket, then the socket must be read before
# the next call to select() to avoid "losing data".  The sets must
# also be constructed anew before each call to select() (see below).
