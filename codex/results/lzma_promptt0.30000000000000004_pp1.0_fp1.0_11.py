import lzma
# Test LZMADecompressor

# The test data is from the xz-utils test suite, which is in the public domain.
# See http://tukaani.org/xz/xz-test-5.2.3.tar.bz2

# The test data is a concatenation of the following files:
#
#  - test/compress/empty.xz
#  - test/compress/alice29.txt.xz
#  - test/compress/asyoulik.txt.xz
#  - test/compress/cp.html.xz
#  - test/compress/fields.c.xz
#  - test/compress/geo.protodata.xz
#  - test/compress/grammar.lsp.xz
#  - test/compress/kennedy.xls.xz
#  - test/compress/lcet10.txt.xz
#  - test/compress/plrabn12.txt.xz
#  - test/compress/ptt5.xz
#  - test
