import mmap
import os
import re
import sys

#
# Constants
#

#
# Globals
#

#
# Functions
#

#
# Classes
#

class Regexp:
    def __init__(self, pattern, flags=0):
        self.pattern = pattern
        self.flags = flags
        self.regexp = re.compile(pattern, flags)

    def match(self, string):
        return self.regexp.match(string)

    def search(self, string):
        return self.regexp.search(string)

    def findall(self, string):
        return self.regexp.findall(string)

    def finditer(self, string):
        return self.regexp.finditer(string)

    def sub(self, repl, string, count=0):
        return self.regexp.sub(repl, string, count)

    def subn(self, repl, string, count=0):
        return self.regexp.subn(repl, string, count)


