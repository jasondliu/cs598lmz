import io
# Test io.RawIOBase

# The io.RawIOBase class is the base class for raw binary I/O.
# It's not meant to be instantiated directly.
# Its purpose is to define the Raw I/O interface,
# and to provide a default implementation of this interface,
# with the exception of readinto() and write().

# To implement a concrete Raw IO class,
# you need to override read(), write() and seek() at a minimum.

# In general, raw binary I/O classes can share most of their implementation.
# The RawIOBase class provides a default implementation which
# reads and writes single bytes through the readinto() and write() methods.
# This implementation is not optimized.

# Note
# The io.RawIOBase class is only meant to be used as a base class.
# It doesn't define the __init__() constructor,
# and it doesn't define the fileno() method.

# It's possible to create a raw binary file on top of a buffered text file,
# using io.TextIOWrapper(io.BufferedRandom(file), encoding='latin-1', newline=
