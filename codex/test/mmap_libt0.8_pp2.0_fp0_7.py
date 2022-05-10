import mmap
import re

class File(object):
    def __init__(self, filename, mode='r'):
        if mode in ('w', 'a'):
            self.f = open(filename, mode)
        else:
            self.f = open(filename, 'r+')
            self.mm = mmap.mmap(self.f.fileno(), 0)

    def write(self, s):
        self.f.write(s)
        self.f.flush()
        if self.mm:
            self.mm.flush()

    def close(self):
        self.f.close()
        if self.mm:
            self.mm.close()

    def read(self):
        return self.mm


# source text format:
#   BEGIN<TAB><SOURCE-TEXT>
#   WORD<TAB><TRANSLATION>
#   END
class TextFormat(object):
    REGEX_OF_BEGIN = r'^BEGIN\t(.*)$';
