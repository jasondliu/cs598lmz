import select
# Test select.select()
#
# The select() function takes three lists of file descriptors and waits until
# some of them become ready for I/O. The first list contains file descriptors
# to be checked for being ready to read, the second contains file descriptors
# to be checked for being ready to write, and the third contains file descriptors
# to be checked for error conditions. The function returns three lists of file
# descriptors: those that are ready to read, those that are ready to write, and
# those that have an error condition.
#
# The following example opens a pipe and a regular file, and then calls select()
# to see if data can be read from the pipe and if the regular file can be read
# from and written to:

import sys, time
from select import select

if len(sys.argv) != 2:
    print >>sys.stderr, 'usage: wait_for_ready_fd.py <filename>'
    sys.exit(2)

filename = sys.argv[1]

# Open the file
f = open(filename, 'r')

