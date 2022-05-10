import bz2
# Test BZ2Decompressor
try:
    bz2.BZ2Decompressor()
    print("Looks good from bz2")
except Exception as e:
    print("No BZ2Decompressor: {}".format(e))
# Test zlib decompression
try:
    zlib.decompress(b'x\x9cK\xcb\xcf\x07\x00\x02\x82PIX')
    print("Looks good from zlib")
except Exception as e:
    print("No ZLIB decompression: {}".format(e))
# Test the snappy library
try:
    # Parse C headers
    snappy.uncompress('\x82SNAPPY\x00\x00\x00\x00\x00\x00\x02\x00\x00')
    print("Looks good from snappy")
except Exception as e:
    print("No SNAPPY: {}".format(e))
# Test the lz4 library
