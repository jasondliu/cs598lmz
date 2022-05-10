import bz2
# Test BZ2Decompressor by providing it with compressed data and decompressing it

original_data = open('/Users/liamconnell/Tutorials/Liams_Python_Tutorials/Resources/data.csv').read()

print('Original length:', len(original_data))

compressed_data = bz2.compress(original_data.encode('utf-8'))

print('Compressed length:', len(compressed_data))

data = bz2.decompress(compressed_data).decode('utf-8')

print('Just decompressed:', len(data))

with bz2.BZ2File('/Users/liamconnell/Tutorials/Liams_Python_Tutorials/Resources/data.csv.bz2', 'w') as f:
    f.write(original_data)

with bz2.BZ2File('/Users/liamconnell/Tutorials/Liams_Python_Tutorials/Resources/data.csv.bz2', 'r') as f:
    bz_data = f
