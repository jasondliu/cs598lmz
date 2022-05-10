import mmap
# Test mmap.mmap()

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

# Create a memory-map to an object.
# The first argument is an integer file descriptor for the file to be memory-mapped.
# The second argument is the length of the mapping (which must be less than or equal to the length of the file).
# The optional arguments flags and prot specify the protection of the mapping (see the Unix man page mmap(2)).
# The optional argument access defines the access to the file.
# The default value is mmap.ACCESS_DEFAULT.
# The optional argument offset is the offset into the file where the mapping starts (defaults to 0).

# If the file is opened in text mode, only offsets returned by tell() are legal.
# Use of other offsets causes undefined behavior.

# Note: The mmap module is only available on Unix and Windows.

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

# Create a memory-map to an object.
# The first argument
