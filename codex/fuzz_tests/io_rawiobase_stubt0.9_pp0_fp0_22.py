import io
class File(io.RawIOBase):
    def __init__(self, file_spec, file_obj, enc=None, newline=None):
        self.file_spec = file_spec
        self.file_obj = file_obj
        self.enc = enc or sys.getdefaultencoding()
        self.newline = newline or "\n"

    def read(self, size=None):
        return self.file_obj.read(size).encode(self.enc, "replace")

    def readline(self, size=None):
        return self.file_obj.readline(size).encode(self.enc, "replace")

    def write(self, buf):
        self.file_obj.write(buf.decode(self.enc, "replace"))

    # TODO: add flush method

    def close(self):
        self.file_obj.close()


def open(file_spec, mode='r', encoding=None, newline=None):
    return File(file_spec, builtins.open(file_spec.to_native(), mode), encoding, newline)
</
