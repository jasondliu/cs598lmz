import lzma
# Test LZMADecompressor object
data = b'12345abcde' * 1024 * 1024 * 10
data = lzma.compress(data)
comp = lzma.LZMADecompressor()
# Try decompressing up to 32 KB of data at a time
for size in range(2**15, 2**17+1, 2**15):
    part = data[:size]
    data = data[size:]
    uncomp = comp.decompress(part)

    if uncomp:
        print('Decompressed %d bytes' % len(uncomp))
# At end of input, the LZMADecompressor may still be buffering data.
# Flush it out.  The empty bytes object (b'') signals EOD.
uncomp = comp.decompress(b'')
if uncomp:
    print('Finished: %d bytes of output' % len(uncomp))

# Using lzma to compress and decompress individual files
with lzma.open('office.xls.lzma', 'w',
               format=lzma.FORMAT_XZ) as
