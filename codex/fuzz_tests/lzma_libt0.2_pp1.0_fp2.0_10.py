import lzma
lzma.decompress(lzma.compress(b'hello world'))

# lzma.compress() and lzma.decompress() support an optional format argument
# that can be used to control the data format used by the functions.
# The default format is lzma.FORMAT_AUTO, which automatically detects the
# file format used by the input.
#
# The other supported formats are lzma.FORMAT_XZ, lzma.FORMAT_ALONE,
# lzma.FORMAT_RAW, and lzma.FORMAT_CHECKED.
#
# The lzma.FORMAT_XZ format is the default file format of the xz utility.
# It is also the default format used by the lzma module when the format
# argument is omitted.
#
# The lzma.FORMAT_ALONE format is a container format that stores a single
# compressed stream. It is mainly useful for embedded applications.
#
# The lzma.FORMAT_RAW format is a container format that stores a single
# compressed stream. It is mainly
