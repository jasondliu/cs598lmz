import lzma
# Test LZMADecompressor
 
comp = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
with open('/dev/null', 'wb') as fnull:
    comp.compress(b'12345678')
    comp.flush(lzma.FLUSH_FULL)
    comp.copy_stream(fnull)
 
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE, memlimit=2**32)
with open('/dev/null', 'wb') as fnull:
    decomp.decompress(comp.stream.read())
    decomp.flush(lzma.FLUSH_FULL)
    decomp.copy_stream(fnull)
</code>

