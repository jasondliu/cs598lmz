import bz2
# Test BZ2Decompressor's __del__ (before exit, or after __exit__)
# by running in a sub-process, so we can catch the exception.
# This is to bypass the exception handler in pythonrun.c.

