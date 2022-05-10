from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYo')

# bz2.decompress(data)
#
# Return the decompressed form of the data.
#
# If data is not a byte string, it will be converted to a byte string using the standard encoding for the platform (see sys.getdefaultencoding()).
#
# Return a byte string containing the uncompressed data corresponding to at least part of the data in string.
#
# The decompressor object can be used to decompress data sequentially. If you want to decompress data in one shot, use the decompress() function instead.
#
# Changed in version 2.5: Added support for the optional argument.
