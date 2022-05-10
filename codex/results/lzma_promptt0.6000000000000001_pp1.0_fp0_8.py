import lzma
# Test LZMADecompressor
with lzma.open('./data/enwik8', mode='rb') as f:
    file_content = f.read()
    print(len(file_content))

lzc = lzma.LZMADecompressor()
result = lzc.decompress(file_content)
print(len(result))

# Test LZMACompressor
with lzma.open('./data/enwik8.xz', mode='wb') as f:
    f.write(result)

with lzma.open('./data/enwik8.xz', mode='rb') as f:
    file_content = f.read()
    print(len(file_content))

lzc = lzma.LZMACompressor()
result = lzc.compress(file_content)
print(len(result))

# Test LZMAFile
with lzma.open('./data/enwik8.xz', mode='rb') as f:
    file_content = f.read()
   
