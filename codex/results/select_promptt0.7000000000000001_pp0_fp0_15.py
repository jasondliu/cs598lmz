import select
# Test select.select()

# This code only works on POSIX systems.

# This test may fail on Windows systems, since select() does not work with pipes
# on Windows.  See the discussion of this issue in the documentation for
# the subprocess module.

# Writes to pipe are atomic, so we can't do partial writes.
# A 1k buffer should be big enough.
BUFSIZE = 1024

# 7 is EOF in ASCII
MSG = b'7'

with open(os.devnull, 'rb') as devnull:
    # Windows creates a non-inheritable handle by default, so
    # explicitly open the handle as inheritable
    r, w = os.pipe()
    r = os.fdopen(r, 'rb', bufsize=0)
    w = os.fdopen(w, 'wb', bufsize=0)
    try:
        input = [devnull, r]
        output = [devnull, w]
        readable, writable, exceptional = select.select(input, output, input)
        print('input   ', readable)
        print('output
