import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('data/tmp/book_uncompressed.txt') as f_in, \
     open('data/tmp/book_compressed.txt.bz2', 'rb') as f_in_bz2, \
     open('data/tmp/book_decompressed.txt', 'wb') as f_out:
    while True:
        chunk = f_in_bz2.read(100)
        if not chunk:
            break
        f_out.write(decompressor.decompress(chunk))
 
# Test BZ2Compressor
with open('data/tmp/book_uncompressed.txt') as f_in, \
     open('data/tmp/book_compressed.txt.bz2', 'wb') as f_out_bz2, \
     bz2.BZ2Compressor(9) as compressor:
    for line in f_in:
        f_out_bz2.write(compressor.compress(line))
    f
