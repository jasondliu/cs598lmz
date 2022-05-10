import bz2
# Test BZ2Decompressor
with open(path, 'rb') as f_in, bz2.BZ2File(path_out, 'wb') as f_out:
    f_out.write(f_in.read())
bz2_decompressor = bz2.BZ2Decompressor()
with open(path, 'rb') as f_in, open(path_out, 'wb') as f_out:
    while True:
        chunk = f_in.read(1024)
        if not chunk:
            break
        f_out.write(bz2_decompressor.decompress(chunk))
bz2_decompressor = bz2.BZ2Decompressor()
with open(path, 'rb') as f_in, open(path_out, 'wb') as f_out:
    for data in iter(lambda: f_in.read(1024), b''):
        f_out.write(bz2_decompressor.decompress(data))
 
import lzma
# Test LZMADecompressor
with open
