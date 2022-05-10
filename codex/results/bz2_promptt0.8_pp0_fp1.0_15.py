import bz2
# Test BZ2Decompressor
data = bz2.BZ2Decompressor()

print('\nSave data to file: ')
# Save data to a file

filename = 'zh_wiki_abstract.txt'
f = bz2.open(filename, 'rb')
file_content = f.read()
f.close()
# Save data
with open('zh_wiki_abstract_compress.txt', 'wb') as f:
    f.write(file_content)
# Delete file
os.remove(filename)

# Test BZ2Compressor
print('\nCompress data: ')
data = bz2.BZ2Compressor()

filename = 'zh_wiki_abstract_compress.txt'
print('Open file: ', filename)
# Open file
print('Read file.......')
f = open(filename, 'rb')
file_content = f.read()
f.close()
# Compress data
print('Compress data.......')
compressed_content = data.compress(file_content)

# Save compress data
filename = 'zh
