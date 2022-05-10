import select
# Test select.select() for reading from a pipe.
#
# In one process, create a pipe, and use a select() on the pipe
# to repeatedly read one byte.
#
# This test is to check if select() will hang with a closed pipe.
# The problem is that the select() in that case returns immediately
# with only the exception bit set.  The following read would block.
#
# This problem was fixed by setting the exception bit in the select
# result even when O_NONBLOCK is set.
#
# Written by Jeff Epler, who hereby places this code into the public
# domain.

# Create a pipe.
r, w = os.pipe()

# Make the read end non-blocking.
fcntl.fcntl(r, fcntl.F_SETFL, os.O_NONBLOCK)

# Set up a select() on the read end of the pipe.
in_fds = [r]
out_fds = []
exc_fds = []

# Keep reading from the pipe until we get a read error.
while 1:
    # Loop
