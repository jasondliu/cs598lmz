import lzma
# Test LZMADecompressor with a decompression object

# First, create a decompression object
d = lzma.LZMADecompressor()

# Then, feed data to it. The compressed data is fed in chunks
# to avoid overloading the decompressor with too much data.
# This is especially important when decompressing large files.
with open('data/xz_test_file.xz', 'rb') as input:
    with open('data/xz_test_file.out', 'wb') as output:
        while True:
            chunk = input.read(1024)
            if not chunk:
                break
            output.write(d.decompress(chunk))
        output.write(d.flush())
 
with open('data/xz_test_file.out', 'r') as f:
    print(f.read())

os.remove('data/xz_test_file.out')

# Test LZMADecompressor with a decompression object

# First, create a decompression object
d = lzma.LZMADecompressor()

