import lzma
lzma.LZMACompressor(format=lzma.FORMAT_XZ)
lzma.LZMADecompressor(format=lzma.FORMAT_XZ)

# zipfile module tests
import zipfile

zipfile.ZIP_STORED
zipfile.ZIP_DEFLATED
zipfile.ZIP64_VERSION
zipfile.ZIP_BZIP2
zipfile.ZIP_LZMA

# This file is not written by the test, so ignore the ResourceWarning.
# The test is checking to see if the file is properly closed.
