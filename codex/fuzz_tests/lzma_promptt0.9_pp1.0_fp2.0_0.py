import lzma
# Test LZMADecompressor and LZMACompressor
assert lzma.decompress(lzma.compress(b'foo')) == b'foo'
with lzma.open("filename", "rb") as lzfile:
    ...
 
# If threads are not used to parallel compress,
# the compressing files in parallel can be of almost no benefit.
# Similarly, decompressing multiple compressed files in parallel
# is likely to be possible only with I/O bound workloads.
#
#  Decompress a file with threading:
with lzma.open("lzfile", "rb") as lzf, open("outfile", "wb") as outfile:
    with threading.Thread(target=outfile.write,
                          args=(lzf.read(65536),)) as t:
        t.start()
        t.join()
 
#  Decompress multiple files from one thread:
def decompress_parallel(lzfiles, threads=3):
    lzfiles[0].threads = threads
    lzfiles[0].read()                   # Fill all
