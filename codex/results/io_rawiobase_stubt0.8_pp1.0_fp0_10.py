import io
class File(io.RawIOBase):
    """A file in the file system."""
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        # Current position in the file
        self.cursor = 0

    def readinto(self, buffer):
        """Reads a buffer into a file."""
        cursor = self.cursor
        data = self.data
        end = min(cursor+len(buffer), self.size)
        data = data[cursor:end]
        self.cursor = end
        # Copy data into the buffer
        buffer[:len(data)] = data
        # Return number of bytes read
        return len(data)
