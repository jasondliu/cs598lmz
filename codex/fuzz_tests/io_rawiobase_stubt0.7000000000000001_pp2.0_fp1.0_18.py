import io
class File(io.RawIOBase):

    """A file object that can be used by mmap.

    It is a wrapper around the system C API for files.
    """

    def __init__(self, name, flag='r', mode=0o777, *,
                 dir_fd=None, effective_ids=False,
                 follow_symlinks=True):
        """Open a file.

        The parameters are the same as os.open() without the dir_fd parameter.
        """
        if dir_fd is not None:
            raise ValueError("dir_fd not supported")
        if effective_ids:
            raise ValueError("effective_ids not supported")
        if not follow_symlinks:
            raise ValueError("follow_symlinks not supported")

        self._name = name
        self._mode = mode
        self._flags = flag

        # We use a list of flags to avoid the problem of having to
        # mask out O_RDONLY etc.
        if 'r' in flag:
            if '+' in flag:
                self._oflags = os.O_RDWR
            else:
               
