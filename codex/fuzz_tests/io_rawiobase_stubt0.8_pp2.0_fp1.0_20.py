import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename

    def fileno(self):
        return os.open(self.filename, os.O_RDONLY)

    def close(self):
        os.close(self.fileno())

    def read(self, size=-1):
        return os.read(self.fileno(), size)
</code>
I tried using <code>open</code> instead of <code>os.open</code>, but then I couldn't call <code>os.close</code> on it. If I call <code>close</code> on the original filehandle, it will close the original filehandle and I won't be able to read from it again.

