import io
class File(io.RawIOBase):
    def write(self, string):
        self.write_out.append(string)
        return len(string)

class Fs(object):
    def __init__(self):
        super().__init__()
        self.fs = {}
        # A list of all the opened file objects.
        self.open_fds = []
    def _find_or_create_entry(self, path):
        cur = self.fs
        for p in pathlib.Path(path).parts[:-1]:
            if p not in cur:
                cur[p] = {}
            cur = cur[p]
    def _find_or_raise_entry(self, path):
        cur = self.fs
        for p in pathlib.Path(path).parts[:-1]:
            if p not in cur:
                raise FileNotFoundError(path)
            cur = cur[p]
        return cur
    def open(self, path, mode = "r"):
        self._find_or_create_entry(path)
        fd = len(self.open_
