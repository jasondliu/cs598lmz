import io
class File(io.RawIOBase):
    _blksize = 512
    _max_read = 32 * 1024

    def __init__(self, disk, partition=1):
        self._disk = disk
        self._partition = partition
        self._block = 0
        self._offset = 0
        self._dir = None
        self._dir_block = 0
        self._dir_ptr = 0

    def _read_dir(self):
        if self._dir is None or self._dir_block != self._block:
            self._dir = self._disk.read_block(self._block, fat=self._partition)
            self._dir_block = self._block
            self._dir_ptr = 0

    def _read_data(self, block):
        return self._disk.read_block(block, fat=self._partition)

    def __iter__(self):
        self._block = self._disk.first_block
        self._offset = 0
        self._dir = None
        self._dir_block = 0
        self._dir_ptr = 0
        return self

    def __next
