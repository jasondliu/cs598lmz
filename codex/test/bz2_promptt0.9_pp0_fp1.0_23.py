import bz2
# Test BZ2Decompressor with an incomplete stream

data = bz2.BZ2Decompressor()
try:
    data.decompress(b"BZh91AY&SY")
except EOFError:
    print("OK")
else:
    print("Failed")
