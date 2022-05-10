from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# #############################################################################
#
# #############################################################################

"""
The lzma module defines the following functions:

compress(data, format=FORMAT_AUTO, check=-1, preset=None, filters=None)

    Return compressed data as a bytes object.

    data
        This can be either a bytes object or a file object.
        If it is a bytes object, it should be of the form returned by the
        compress() function.

    format
        Specifies the container format to use for the output.
        This can be FORMAT_AUTO, FORMAT_XZ, FORMAT_ALONE, FORMAT_RAW, or
        FORMAT_CHECK. The default is FORMAT_AUTO.

    check
        Specifies the integrity check to use. This can be either CHECK_NONE,
        CHECK_CRC32, CHECK_CRC64, CHECK_SHA256. The default is CHECK_NONE.

    preset
        The preset to use. This can be any integer in the range
        0-9 or PRES
