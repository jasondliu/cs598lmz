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
with open(support.TESTFN, "wb") as fp:
    with zipfile.ZipFile(fp, mode="w") as zipfp:
        zipfp.writestr("somefile.txt", b"bogus")

# Issue #7524: Tests that writing ZipInfo instances with an explicit
# date time works.
with open(support.TESTFN, "wb") as fp:
    with zipfile.ZipFile(fp, mode="w") as zipfp:

