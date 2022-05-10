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
