import io
class File(io.RawIOBase):
    def __init__(self, name, mode, encoding=None, errors=None, newline=None,
                 closefd=True, opener=None, *, opener_callback=True):
        pass
    def __del__(self, *ignore):
        """Finalizer.
        Some file-like object use a finalizer, so this must exist.
        """
        pass
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False
    def close(self):
        """
        Close the file.  A closed file cannot be used for further I/O operations.
        close() may be called more than once without error.
        """
        pass
    def fileno(self):
        r"""
        Return the file descriptor that is used by the underlying implementation,
        with inheriting classes if present.
        This description is copied from io.RawIOBase.
        """
        pass
    def flush(self):
        """
        Flush write buffers, if applicable
