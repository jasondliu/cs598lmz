import bz2
# Test BZ2Decompressor with bogus input parameters
try:
    bz2.BZ2Decompressor(bufsize=30, compresslevel=4)
    raise RuntimeError("bufsize not checked")
except ValueError:
    pass
try:
    bz2.BZ2Decompressor(bufsize="test")
    raise RuntimeError("bufsize doesn't accept str")
except TypeError:
    pass
try:
    bz2.BZ2Decompressor(bufsize=b"test")
    raise RuntimeError("bufsize doesn't accept byte")
except TypeError:
    pass
with bz2.BZ2Decompressor() as decomp:
    try:
        decomp.decompress(-1, -2)
        raise RuntimeError("size parameter not checked")
    except Exception:
        pass
# Test BZ2Compressor with bogus input parameters
try:
    bz2.BZ2Compressor(compresslevel=-1, bufsize=1)
    raise RuntimeError("compresslevel not checked")
except ValueError:
    pass
try:
    bz2.BZ
