import bz2
# Test BZ2Decompressor with a BZ2File
# to make sure it works as expected
with BZ2File('small.bz2', 'rb') as f:
    decomp = BZ2Decompressor()
    print(b'Data decompressed:', decomp.decompress(f.read()))
# Test Decompressor with a file from a network
# connection that's broken into multiple chunks

# Make a handler for decoding gzip data
gzip_handler = UnzipWrapper(gzip.decompress)
# Make a response that is gzip encoded
gzipped_response = gzip_handler.fetch(
    'http://httpbin.org/gzip')
# And a handler for decoding bz2 data
bz2_handler = UnzipWrapper(bz2.decompress)
# Make a response that is bz2 encoded
bzipped_response = bz2_handler.fetch(
    'http://httpbin.org/gzip')
# Print out both; they're the same
print(gzipped_response)
print('-' * 75)
print(bzipped
