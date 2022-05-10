import codecs
codecs.register_error("gdal_error", codecs.replace_errors)

import gdal, gdalconst
gdal.UseExceptions()
gdal.AllRegister()

# TODO: Check that all expected GDAL/Python modules are present

# only for Python < 2.5 compatibility.  Not sure if this is kosher...
if sys.version_info[1] < 5:

    try:
        import md5
        md5_constructor = md5.new
    except ImportError:
        import hashlib
        md5_constructor = hashlib.md5

    class sha1(object):
        """This class implements the SHA-1 algorithm.

        SHA-1 hashes a sequence of bits and produces a 160-bit
        (20-byte) hash value known as a message digest. It is
        slightly stronger than the MD5 algorithm. This class is
        a subclass of object, with no public methods or
        attributes beyond those of the base class.
        """

        # The size of the input is stored as a 64-bit little-endian integer
        digest_size = 20

        # TODO
