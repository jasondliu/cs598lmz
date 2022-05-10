import mmap
# Test mmap.mmap(0, 1, "map")
# ERROR: Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: invalid buffer size
# 
# Note that this behaviour doesn't match the tested version of Python on
# Debian (reports OverflowError) or the behaviour of Python 2.7 or later.
