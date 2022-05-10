import io
class File(io.RawIOBase):
    def fileno(self):
        """Return the fileno() of the underlying file."""
        return self.fd

    def readable(self):
        """Return False if this stream cannot be read from."""
        return self.mode in ("r", "w+")

    def writable(self) -> bool:
        """Return False if this stream cannot be written to."""
        return self.mode in ("w", "w+")

    def seekable(self) -> bool:
        return False

    def close(self) -> None:
        """Flush and close this stream.

        This method has no effect if the file is already closed.
        """
        # pylint: disable=attribute-defined-outside-init
        if self.fd is None:
            return
        # pylint: enable=attribute-defined-outside-init
        self.flush()
        os.close(self.fd)
        self._reset()

    def _checkClosed(self, msg=None):
        """Internal: raise an ValueError if file is closed"""
        if self.fd is None
