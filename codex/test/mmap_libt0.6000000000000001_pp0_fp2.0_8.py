import mmap
import re
import glob
import sys

# pylint: disable=broad-except

class Scanner(object):
    def __init__(self, pattern, filename):
        self.pattern = re.compile(pattern)
        self.filename = filename
        self.matches = []

    def scan(self):
        with open(self.filename, "rb") as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            self.mm = mm
            self.scanner = re.Scanner([
                (self.pattern, self.match),
            ])
            self.scanner.scan(mm)

    def match(self, scanner, token):
        self.matches.append((token, scanner.match.start(), scanner.match.end()))
        return True

    def __iter__(self):
        return iter(self.matches)

    def find(self, callback):
        for m in self.matches:
            if callback(m):
                return m

