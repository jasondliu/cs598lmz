import io
# Test io.RawIOBase
# https://docs.python.org/3/library/io.html#io.RawIOBase

# Basic io.RawIOBase Interaction
# https://pymotw.com/3/io/io.RawIOBase.html

# io.TextIOBase
# https://docs.python.org/3/library/io.html#text-i-o

# Basic io.TextIOWrapper
# https://pymotw.com/3/io/io.TextIOWrapper.html


# https://docs.python.org/3/library/io.html#io.RawIOBase.readinto
# readinto(b)
# Read bytes into a pre-allocated, writable bytes-like object b, and return the number of bytes read.
#
# This can be used to avoid allocating a temporary bytes object when reading from a sequence of buffers,
# for example when decoding I/O chunk by chunk into a StringIO:

# def read_all(f, n, f_len):
#     all_data = []
#     while n < f
