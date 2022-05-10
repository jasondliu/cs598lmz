import bz2
bz2_comp = bz2.BZ2Compressor()
bz2_comp.compress('a'*10**6)
print("Done.\n")

print("Compressing with lzma:")
import lzma
lzma_comp = lzma.LZMACompressor()
lzma_comp.compress('a'*10**6)
print("Done.\n")

print("Compressing with zlib:")
import zlib
zlib_comp = zlib.compressobj(level=1)
zlib_comp.compress('a'*10**6)
print("Done.\n")

print("Compressing with gzip:")
import gzip
gzip_comp = gzip.GzipFile(fileobj=gzip.BytesIO(), mode="w")
gzip_comp.compress('a'*10**6)
print("Done.\n")

print("Compressing with blosc:")
import blosc
blosc_comp = blosc.compressobj(clevel=1, cname="sn
