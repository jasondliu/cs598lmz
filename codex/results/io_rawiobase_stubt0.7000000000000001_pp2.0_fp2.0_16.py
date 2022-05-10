import io
class File(io.RawIOBase):
    """
    File wrapper for stream with name and mode.
    """
    def __init__(self, stream, name, mode):
        """
        Constructor.
        :param stream: stream.
        :param name: file name.
        :param mode: file mode.
        """
        self._stream = stream
        self._name = name
        self._mode = mode
    def __enter__(self):
        """
        Enter method for context manager.
        :return: file.
        """
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit method for context manager.
        :param exc_type: exception type.
        :param exc_value: exception value.
        :param traceback: exception traceback.
        :return: None.
        """
        self.close()
    def readable(self):
        """
        Readable method.
        :return: readable.
        """
        return self._stream.readable()
    def writable(self):
        """
        Writable method.
