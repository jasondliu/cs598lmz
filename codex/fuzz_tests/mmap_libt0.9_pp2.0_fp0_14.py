import mmap

from .utils import (memory_map, chrW)


class Completions(object):

    def __init__(self, filename):
        self.SetMax(10)
        self.filename = filename
        self.data = self.read_data(filename)

    def SetMax(self, m):
        self.completion_type = "|"
        self.max_entries = m

    def read_data(self, filename):
        with open(filename, "rb") as handle:
            content = handle.read()

            # see http://bugs.python.org/issue5874
            mm = memory_map(len(content), handle.fileno())
            mm.write(content)
            content = mm
        return content

    def completions(self, prefix):
        for m in re.finditer(b"^(" + re.escape(chrW(prefix)) + b".*)\n",
                             self.data,
                             # dont match empty lines
                             re.MULTILINE | re.DOTALL):
            yield m
