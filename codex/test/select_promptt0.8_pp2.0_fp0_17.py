import select
# Test select.select() for IO objects

import sys, os, time
from test.support import verbose, findfile
from test.script_helper import assert_python_ok

# XXX For now, use only the default select implementation
# import select
# select_implementation = select.select_implementation
select_implementation = None
if select_implementation and select_implementation != "default":
    verbose("Testing only the default select() implementation")
    raise unittest.SkipTest(
        "Testing only the default select() implementation")

# Create a pipe, and fill the output side so we can test that select() doesn't
# indicate it's ready to read until there's enough space to do so.
r, w = os.pipe()
for i in range(100):
    os.write(w, b"x")

# Open a text file and a binary file for testing
f = open(findfile('select_file'), 'rb')
f2 = open(findfile('select_file'), 'r')

# Sever the stderr pipe from the parent, so we can catch write errors in the
