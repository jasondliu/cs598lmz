import lzma
# Test LZMADecompressor
with open('data/lzma_compressed.xz', 'rb') as f_in:
    with lzma.open(f_in) as f_out:
        file_content = f_out.read()
        print(file_content)

# Test LZMACompressor
with open('data/lzma_compressed.xz', 'wb') as f_out:
    with lzma.open(f_out, 'w') as f_in:
        f_in.write(b'This is a test')
 
# Test LZMAFile
with lzma.open('data/lzma_compressed.xz') as f:
    file_content = f.read()
    print(file_content)

# Test LZMAFile with mode
with lzma.open('data/lzma_compressed.xz', mode='wt') as f:
    f.write('This is a test')

# Test LZMAFile with preset
with lzma.open('data/lzma_compressed.
