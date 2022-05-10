import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()
with bz2.BZ2File('data/enwik9.bz2', 'r') as file:
    for _ in range(5):
        block = file.read(1024)
        text = bz2_decompressor.decompress(block)
        print(text)

# Test BZ2Compressor

bz2_compressor = bz2.BZ2Compressor()
with bz2.BZ2File('data/enwik9.new.bz2', 'w') as file:
    for _ in range(5):
        text = 'Some text to compress\n'
        file.write(bz2_compressor.compress(text.encode('utf-8')))
        file.flush()
 
# Test BZ2File

with bz2.BZ2File('data/enwik9.bz2', 'r') as file:
    for _ in range(5):
        block = file.read(1024
