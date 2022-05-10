import io
class File(io.RawIOBase):
    """A raw file object."""

    # The file operations that are defined to operate on a text file
    # operate on a file in the corresponding binary mode.
    _CHUNK_SIZE = 8 * 1024

    def _set_read_only(self):
        # By default, regular files are mutable.
        pass

    def _set_read_write(self):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        self.seek(0, io.SEEK_CUR)
        # and the file is writable...
        self.mode = 'r+b'
        # reset the readahead buffer, if any
        self.buffer.truncate(0)
        self.raw.truncate(self.tell())

    def _set_read_only_mmap(self):
        # mmaps are always read-only
        self.mode = 'r'
        self.seek(0)

    def _set_read_write_mmap(self):
        raise io.UnsupportedOperation('mmap can only read')


