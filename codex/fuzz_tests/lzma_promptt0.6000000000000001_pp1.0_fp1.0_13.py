import lzma
# Test LZMADecompressor
with open('lzma_compressed.bin', 'rb') as infile:
    with lzma.open(infile, 'rb') as decomp:
        print(decomp.read())

# Test LZMACompressor
with open('lzma_compressed.bin', 'wb') as outfile:
    with lzma.open(outfile, 'wb') as comp:
        comp.write(b'Hello World!')

# Test LZMADecompressor
with open('lzma_compressed.bin', 'rb') as infile:
    with lzma.open(infile, 'rb') as decomp:
        print(decomp.read())

# Test LZMACompressor
with open('lzma_compressed.bin', 'wb') as outfile:
    with lzma.open(outfile, 'wb') as comp:
        comp.write(b'Hello World!')

# Test LZMADecompressor
with open('lzma_compressed.bin', 'rb') as infile:
   
