import socket
socket.if_indextoname(3)

# If you have a socket, you can use its fileno() method to get the underlying file descriptor.
# Then you can use that with the fcntl() function.
import fcntl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))

# Make the socket non-blocking
fcntl.fcntl(s.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)

# Make the socket close-on-exec
flags = fcntl.fcntl(s.fileno(), fcntl.F_GETFD)
flags |= fcntl.FD_CLOEXEC
fcntl.fcntl(s.fileno(), fcntl.F_SETFD, flags)

# The ioctl() function is used to control device parameters.
# It is available on many devices, including serial ports, sound cards, and disk drives.

# The fcntl() function can also be
