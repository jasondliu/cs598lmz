import select
# Test select.select
def fileno(file_or_fd):
    fd = getattr(file_or_fd, 'fileno', lambda: file_or_fd)()
    if not isinstance(fd, int):
        raise ValueError("Expected a file (`.fileno()`) or a file descriptor")
    return fd

fileno(sys.stdin)
# Test select.select
# Test cases : File descriptor, list of file descriptors and poll objects.

# File descriptor:
mysocket = socket(AF_INET, SOCK_STREAM)
# default value of the socket timeout is None, we can set it at will.
print(mysocket.gettimeout())
mysocket.settimeout(10)
# fileno is a method on socket socket.fileno()
# fileno is an attribute on file (read only).
fileno(mysocket)
# https://stackoverflow.com/questions/13431423/python-fileno-attribute
# https://stackoverflow.com/questions/366693/what-is-the-meaning-of-pyth
