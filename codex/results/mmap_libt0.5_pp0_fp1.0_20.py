import mmap
import re
import subprocess
import sys
import time

#
# Globals
#

#
# Functions
#

def usage():
    print "Usage: %s [-d] <file> <pattern> <replacement>" % sys.argv[0]
    print "  -d  dry run"
    sys.exit(1)

#
# Main
#

if len(sys.argv) < 4:
    usage()

dry_run = False
if sys.argv[1] == "-d":
    dry_run = True
    sys.argv.pop(1)

filename = sys.argv[1]
pattern = sys.argv[2]
replacement = sys.argv[3]

pattern = re.compile(pattern)

# Create a temporary file
fd, tmp_filename = tempfile.mkstemp()

# Open the temporary file
tmp_file = os.fdopen(fd, 'w')

# Open the file
with open(filename, 'r+') as f:
    # Memory
