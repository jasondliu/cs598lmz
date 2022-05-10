import mmap
# Test mmap.mmap()
#
# This test is based on the following example:
# http://www.python.org/doc/2.5.2/lib/mmap-example.html

import mmap
import os
import struct
import tempfile

def test_mmap():
    # Create a temporary file and write some data to it
    fd, filename = tempfile.mkstemp()
    os.close(fd)
    with open(filename, "wb") as f:
        f.write(b"Hello world!")

    # Open the file for reading
    f = open(filename, "r+b")

    # Create a mmap'ed file that can be written to and read from
    m = mmap.mmap(f.fileno(), 0)

    # Read the content via standard file methods
    assert f.read(len(b"Hello world!")) == b"Hello world!"

    # Read the content via the mmap'ed file
    assert m[:len(b"Hello world!")] == b"Hello world!"

    # Update content using slice notation
    # Note
