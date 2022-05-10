import io
# Test io.RawIOBase.

# This class implements all the hooks required so that it can be used with
# routines that perform I/O operations on file-like objects.  Only
# RawIOBase.write() is implemented.

# devnull is the traditional name for a device that discards everything.
import os
devnull = open(os.devnull, "w")

