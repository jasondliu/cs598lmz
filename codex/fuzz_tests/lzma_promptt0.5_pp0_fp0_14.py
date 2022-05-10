import lzma
# Test LZMADecompressor
print('LZMADecompressor:')
decompressor = lzma.LZMADecompressor()
with open('lorem.txt.xz', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content).decode('utf-8'))
    print(decompressor.unused_data)

# Test LZMADecompressor.decompress
print('\nLZMADecompressor.decompress:')
with lzma.open('lorem.txt.xz') as f:
    file_content = f.read()
    print(file_content.decode('utf-8'))

# Test LZMAFile
print('\nLZMAFile:')
with lzma.open('lorem.txt.xz') as f:
    file_content = f.read()
    print(file_content.decode('utf-8'))

# Test LZMAError
#print('\nLZMAError:')
