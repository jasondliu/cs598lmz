import select
# Test select.select

import select
import sys

# Use select() to wait until there is input on stdin
print("Waiting for input . . .")
rlist, wlist, xlist = select.select([sys.stdin], [], [])
print("Input detected!")

# The input file descriptor is 0, so it will be in the list rlist
assert 0 in rlist


# Use select() to wait until the file descriptor is ready to be read
print("Waiting for the file to be ready . . .")
rlist, wlist, xlist = select.select([open('/tmp/foo', 'rb')], [], [])
print("File is ready!")


# Use select() to wait until the file descriptor is ready to be read
