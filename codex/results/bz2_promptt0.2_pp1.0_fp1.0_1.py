import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f_in:
    with open('data/enwik8.txt', 'wb') as f_out:
        for chunk in iter(lambda: f_in.read(1024), b''):
            f_out.write(bz2_decompressor.decompress(chunk))
 
# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f_in:
    with open('data/enwik8.txt', 'wb') as f_out:
        for chunk in iter(lambda: f_in.read(1024), b''):
            f_out.write(chunk)
 
# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f_in:
    with open('data/enwik8.txt', 'wb
