import mmap
import re
import sys

#
# Global variables
#

#
# Functions
#

#
# Main
#

#
# Parse command line
#

if len(sys.argv) != 2:
    print("Usage: {} <file>".format(sys.argv[0]))
    sys.exit(1)

filename = sys.argv[1]

#
# Open file
#

with open(filename, "r") as f:
    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    #
    # Find all matches
    #

    pattern = re.compile(br"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
