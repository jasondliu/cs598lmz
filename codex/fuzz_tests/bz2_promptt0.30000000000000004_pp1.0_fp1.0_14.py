import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    for chunk in iter(lambda: f.read(100 * 1024), b''):
        text = bz2_decompressor.decompress(chunk)
        print(text)
        if len(text) > 0:
            break

# Test BZ2File
with bz2.BZ2File('data/enwik8.bz2', 'r') as f:
    for line in f:
        print(line)
        break

# Test BZ2Compressor
bz2_compressor = bz2.BZ2Compressor()

with open('data/enwik8.bz2', 'rb') as f_input, open('data/enwik8_copy.bz2', 'wb') as f_output:
    for chunk in iter(lambda: f_input.read(100 * 1024), b''):
        f_output.write(bz2_
