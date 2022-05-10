import lzma
lzma.open

# lzma.open(filename, mode="r", format=None, check=-1, preset=None, filters=None)

# filename can be an actual filename (a str or bytes object), or an existing file object to read from or write to.

# mode can be either "r" for reading (default), "w" for (over)writing, or "a" for appending.

# format must be given for writing, and can be "xz", "lzma", or None (same as "xz"). For reading, format can be None or an empty string, in which case the format is automatically detected.

# check can be given to control the integrity check that is performed on the uncompressed data. It can be given as an integer or as a string.

# preset is an integer in the range 0-9 or an LZMA compression preset string.

# filters is an optional list of dictionaries, each specifying one LZMA filter.

# Example:

# >>> import lzma
# >>> with lzma.open("foo.xz", "w") as f:
