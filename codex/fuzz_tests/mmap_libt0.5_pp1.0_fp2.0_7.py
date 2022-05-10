import mmap
import os
import re
import sys

#
#   Globals
#

#
#   Constants
#

#
#   Functions
#

def parse_file(f):
    result = ""
    while True:
        line = f.readline()
        if not line:
            break
        line = line.rstrip()
        if line.startswith("#"):
            continue
        if line.startswith("\n"):
            continue
        if re.match(r"^\s+$", line):
            continue
        if re.match(r"^\s*$", line):
            continue
        if re.match(r"^\s*#", line):
            continue
        if re.match(r"^\s*\n$", line):
            continue
        if re.match(r"^\s*$\n$", line):
            continue
        result += line + "\n"
    return result

#
#   Classes
#

#
#   Mainline
#

if
