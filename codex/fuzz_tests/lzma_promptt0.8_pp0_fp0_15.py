import lzma
# Test LZMADecompressor by reading all of stdin,
# decompressing it, and writing the result to stdout.
with lzma.open('lzma_file', mode='r') as f:
    file_content = f.read()
print(file_content)

# it's a good idea to do that when you need to process a lot of data,
# as LZMADecompressor is able to decompress data incrementally


# writing data

data = b"Now is the time for all good men to come to the aid of their country."
with lzma.open('lzma_file', mode='w') as f:
    f.write(data)

with lzma.open('lzma_file', mode='w') as f:
    f.write(b"Now is the time for all good men to come to the aid of their country.")

with lzma.open('lzma_file', mode='w') as f:
    f.write(b"Now is the time for all good men to come to the aid of their country.")

# You can use action
