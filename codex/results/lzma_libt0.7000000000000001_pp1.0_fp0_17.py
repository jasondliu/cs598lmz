import lzma
lzma.LZMAError
import pickle
pickle.UnpicklingError
import sqlite3
sqlite3.OperationalError
import zlib
zlib.error
EOF

# coverage.py is a pain in the ass.  We want to check that it can be
# imported, but we don't want to run its main() function.  It must be
# run as __main__, so we can't import it directly.  And if it finds a
# .coveragerc file in the current directory, it will stop execution
# and print a message, which is not the behavior we want.  So we need
# to import it by running a subprocess.

import coverage
import subprocess
import sys

try:
    # Remove the .coveragerc file if it exists.
    try:
        os.remove(".coveragerc")
    except OSError:
        pass

    # We are going to run coverage as __main__, but we don't want it to
    # find the coverage.py file that we happen to be running.  So we add
    # the directory above
