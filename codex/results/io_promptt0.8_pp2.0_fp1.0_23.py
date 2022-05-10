import io
# Test io.RawIOBase behavior

import os.path
import sys

from test import support
from test.support import os_helper

error = IOError

#
# Utility functions

def create_file(fname, lines):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(''.join(lines))

def check_file(fname, lines):
    with open(fname, 'r', encoding='utf-8') as f:
        check_lines(f, lines)

def check_lines(f, lines):
    got_lines = f.readlines()
    assert got_lines == lines, "readlines wrong"
    f.seek(0)
    got_lines = []
    while True:
        c = f.readline()
        if c == '':
            break
        got_lines.append(c)
    assert got_lines == lines, "readline wrong"
    f.seek(0)
    got_lines = f.read().split("\n")
    assert got_lines == lines,
