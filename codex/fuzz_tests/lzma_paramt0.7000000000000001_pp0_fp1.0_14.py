from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# write data to file
with open('file.txt', 'wb') as f:
    f.write(compressed)

# read data from file
with open('file.txt', 'rb') as f:
    compressed = f.read()

# decompress
data = LZMADecompressor().decompress(compressed)

# decompress and write in chunks
with open('file.txt', 'rb') as f_in:
    with open('file_out.txt', 'wb') as f_out:
        decompressor = LZMADecompressor()
        for chunk in iter(lambda: f_in.read(1024*1024), b''):
            f_out.write(decompressor.decompress(chunk))
        f_out.write(decompressor.flush())
</code>

