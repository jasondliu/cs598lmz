import lzma
# Test LZMADecompressor
print ("  Testing lzma ...")
try:
    dec = lzma.LZMADecompressor()
    print(dec.format)
    print(dec.decompress(b'').decode("utf-8"))
except Exception as e:
    print ("Error: {}".format(e))

print ("\n=== Testing base64 ...")
try:
    import base64
    print("base64", base64.b64decode(b'').decode("utf-8"))
except Exception as e:
    print ("Error: {}".format(e))

print("\n=== Testing zlib ...")
try:
    import zlib
    # Test ZLIBDecompressor
    dec = zlib.decompressobj()
    print(dec.decompress(b'').decode("utf-8"))
except Exception as e:
    print ("Error: {}".format(e))

print("\n=== Testing math ...")
try:
    import math
    print(math.acos(0.0))
    print(math.asin(
