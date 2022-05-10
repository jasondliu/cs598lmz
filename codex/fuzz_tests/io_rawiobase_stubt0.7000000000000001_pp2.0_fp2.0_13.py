import io
class File(io.RawIOBase):
    """
    Class to simplify working with files that
    need to be shared between multiple processes
    """
    def __init__(self, lock, filename, mode='r', buffer_size=1):
        """
        mode is the mode to open the file with
        buffer_size is the buffer size to use
        """
        self.lock = lock
        self.filename = filename
        self.mode = mode
        self.buffer_size = buffer_size
        self.file = None
        self.closed = True #Initially closed

    def acquire(self):
        """
        Acquires the lock
        """
        return self.lock.acquire()

    def release(self):
        """
        Releases the lock
        """
        return self.lock.release()

    def open(self):
        """
        Opens the file with the mode specified
        """
        self.file = open(self.filename, self.mode)
        self.closed = False

    def close(self):
        """
        Closes the file
        """
        if self.closed:
            raise Value
