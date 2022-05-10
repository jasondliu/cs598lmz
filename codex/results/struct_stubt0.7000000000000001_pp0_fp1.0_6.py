from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'c'
s.size = 1

def find_next_free(n, size=s.size, format=s.format):
    """
    Find the next unused file descriptor.

    :param n: File descriptor to start search from
    :param size: Size of the file descriptor in bytes
    :param format: Format of the file descriptor
    :return: The next unused file descriptor
    """
    while True:
        try:
            os.read(n, size)
        except OSError, e:
            if e.errno == errno.EBADF:
                return n
            raise
        n += 1


def get_free_list(pid, num_files=10):
    """
    Find a list of free file descriptors.
    """
    try:
        os.read(num_files, 1)
    except OSError, e:
        if e.errno == errno.EBADF:
            return range(num_files)
        raise
    return []


def get_free_fd(pid
