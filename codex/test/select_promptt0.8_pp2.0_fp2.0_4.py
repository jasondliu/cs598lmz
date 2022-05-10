import select
# Test select.select()
# Select is on of the few good things in Python ;-)
# You can run this test while doing:
#   python -m tty.test_tty -v

from test import support
from test.support import bigmemtest

# Generate a unique filename
import tempfile
TESTFN = tempfile.mktemp()

# Open in text mode by default:
fp = open(TESTFN, "wb")

# File descriptors
stdin  = 0
stdout = 1
stderr = 2

def check(args, expected):
    r, w, x = select.select(args, (), ())
    if (r, w, x) != expected:
        print("Expected %s, got %s" % (expected, (r, w, x)))

# ----------------------------------------------------------------------
# Basic tests, using stdin and stdout

# We don't have input, so nothing should be available:
check([stdin], ([], [], []))

# Write something to stdout and test that it is available:
fp.write(b"a")
