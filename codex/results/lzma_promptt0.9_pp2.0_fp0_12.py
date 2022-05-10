import lzma
# Test LZMADecompressor for read(0) function
#
# Any read(0) operation should return an empty bytes object.
#
dcomp = lzma.LZMADecompressor()
# test it with a new uncompressed stream
this_stream = dcomp.decompress(b'foo')
assert(this_stream == b'foo')
assert(dcomp.unused_data == b'')
assert(dcomp.read(0) == b'')
dcomp.decompress(b'bar')
assert(this_stream == b'foobar')
assert(dcomp.read(0) == b'')

# test it with a new compressed stream
dcomp = lzma.LZMADecompressor()
dcomp.decompress(b'xyzzy\x01')
assert(dcomp.unused_data == b'')
assert(dcomp.read(0) == b'')
dcomp.decompress(b'bar\x00')
assert(dcomp.unused_data == b'bar\x00')
assert(dcomp.decompress
