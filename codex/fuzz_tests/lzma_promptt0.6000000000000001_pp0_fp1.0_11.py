import lzma
# Test LZMADecompressor.eof
# This file was generated from test/test_lzma.py
# with the following command:
#   ./python -m test.pytest -s test/test_lzma.py::test_eof
#
# The original file is a valid xz stream.
# The last byte was changed to corrupt the stream.
#
# Note that python -m test.test_lzma uses the system liblzma if available.
# If the system liblzma is too new for this test,
# it will fail with LZMAError: Input format not supported by decoder
#
# The file was generated with these commands:
#   dd if=/dev/urandom of=truncated.xz bs=1048576 count=10
#   dd if=/dev/zero of=truncated.xz bs=1 seek=10485760 count=1 conv=notrunc
#
# The file is 10 MB.
# It has a 10 byte header, 1 byte footer and 10485739 bytes of random data.
# The footer byte is 0x00
