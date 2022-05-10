import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        super().__init__(*args, **kwargs)

    def close(self):
        if self.closed:
            return
        try:
            if hasattr(self.file, 'close'):
                self.file.close()
        finally:
            super().close()

    @property
    def closed(self):
        return super().closed or (hasattr(self.file, 'closed') and self.file.closed)

    def fileno(self):
        if hasattr(self.file, 'fileno'):
            return self.file.fileno()
        return super().fileno()

    def flush(self):
        if hasattr(self.file, 'flush'):
            self.file.flush()

    def isatty(self):
        if hasattr(self.file, 'isatty'):
            return self.file.isatty()
        return super().isatty()

    @property
    def mode(self):
       
