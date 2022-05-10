import bz2
# Test BZ2Decompressor
dec = bz2.BZ2Decompressor()
data = open('./data/data.txt.bz2', 'rb').read()
dec_out = dec.decompress(data)
dec_out.decode('utf-8')

# Test BZ2Compressor
data = 'Hello world! This is a test.'
comp = bz2.BZ2Compressor()
comp.compress(data.encode('utf-8'))

# Use context manager
with open('./data/data.txt.bz2', 'rb') as in_file, open('./data/data.txt', 'wb') as out_file:
    bz2_dec = bz2.BZ2Decompressor()
    data = in_file.read(100000)
    while data:
 
