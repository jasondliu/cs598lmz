import bz2
bz2.decompress(b)

bz2.compress( b'' )

"bz2.BZ2Decompressor.decompress(data)"
# bz2.BZ2Decompressor.flush(length=0)

# Writing compressed data to a file
"f = open('file.bz2', 'wb')"
"compressor = bz2.BZ2Compressor()"
"for data in pieces:".ljust( 4 ) + """
    compressed = compressor.compress(data)
    if compressed:
        f.write(compressed)
    else:
        f.write(data)"""
"f.write(compressor.flush())"

# Reading compressed data from a file
"f = open('file.bz2', 'rb')"
"decompressor = bz2.BZ2Decompressor()"
"while True:".ljust( 4 ) + """
    block = f.read(1024)
    if not block:
        break
    output = decompressor.decompress(block)
    if
