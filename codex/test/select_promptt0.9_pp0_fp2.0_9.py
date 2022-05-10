import select
# Test select.select to figure out whether a file is available to read.

# Parent/child reading and writing using a pipe.
# Parent writes to pipe, child reads from it and prints.

import os
# Spawn a child with a pipe to read from.
# Pipe is just a pair of ints, the read end and the write end.

r, w = os.pipe()  # Parent reads from r, child writes to w.
processid = os.fork()
if processid:
    # This is the parent process.
    # Close child's side of pipe, and use own side for reading.
    os.close(w)
    r = os.fdopen(r)
    whentoread = select.select([r], [], [])
    if whentoread[0]:
        # If select indicates the file is available for reading, read it.
        data = r.read()
