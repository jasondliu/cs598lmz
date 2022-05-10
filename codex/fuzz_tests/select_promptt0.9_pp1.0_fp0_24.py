import select
# Test select.select with the duplicate of the standard input file.
import sys
import os

# select should just return the *objects* passed in, even if they are
# duplicates.
f = os.fdopen(os.dup(sys.stdin.fileno()))
rfds, wfds, xfds = select.select([sys.stdin, f], [], [])
assert rfds == [sys.stdin, f]
f.close()
