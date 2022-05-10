import io
class File(io.RawIOBase):
    """A file-like object that uses mmap for its backing store.
    """

    def __init__(self, path, mode='r+', access=mmap.ACCESS_WRITE, offset=0, size=0, tagname=None):
        """
        Create a new File object.

        Args:
            path (str): The path to open.
            mode (str): The mode to open the file. Must start with ``r`` or ``w``.
                Additional mode characters are passed to `mmap`.
                On Windows, `mode` is ignored and the file is always opened for
                read-write access.
            access (mmap.ACCESS_*): The type of access to the underlying file.
                This is ignored on Windows.
            offset (int): The offset in the file, in bytes.
            size (int): The size of the file mapping, in bytes.
            tagname (str): The identifier for the file mapping object.

        Raises:
            ValueError: if the mode is not read-only, write-only, or read-write
                and the platform is Windows
