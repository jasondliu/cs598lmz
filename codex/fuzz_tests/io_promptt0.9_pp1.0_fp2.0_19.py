import io
# Test io.RawIOBase.

# This class implements all the hooks required so that it can be used with
# routines that perform I/O operations on file-like objects.  Only
# RawIOBase.write() is implemented.

# devnull is the traditional name for a device that discards everything.
import os
devnull = open(os.devnull, "w")

with open(os.devnull, "w") as f:
    # Write some text to the file.
    f.write(b"x" * 1000 + "\n")

    # Find out how much was written.
    f.tell()

with open(os.devnull, "r") as f:
    # Read some text from the file.
    f.read(10)

    # Find out how much was read.
    f.tell()

with open(os.devnull, "w") as f:
    # Get the file's current position in bytes.
    f.tell()

    # Change the file's position.
    f.seek(10)

with open(os.devnull, "w+") as f
