import bz2
# Test BZ2Decompressor
bz2part = recv_partial(512)

try:

    dc = BZ2Decompressor()
    print(dc.decompress(bz2part))
except OSError:
    # Something went wrong
    print("BZ2DecompressorError")
 
# Test BZ2Decompressor
bz2part = recv_partial(512)
dc = BZ2Decompressor()

try:
    print(dc.decompress(bz2part))
except EOFError:
    print("EOFError")
