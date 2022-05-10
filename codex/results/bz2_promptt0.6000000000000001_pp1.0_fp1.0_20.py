import bz2
# Test BZ2Decompressor

# Initialize decompressor
decompressor = bz2.BZ2Decompressor()

# Decompress first 1 KB of file
with open('data.bz2', 'rb') as f:
    file_content = f.read(1024)
    decompressed_data = decompressor.decompress(file_content)
    print(len(decompressed_data))
# Decompress all file

# Initialize decompressor
decompressor = bz2.BZ2Decompressor()

# Decompress all file
with open('data.bz2', 'rb') as f:
    file_content = f.read()
    decompressed_data = decompressor.decompress(file_content)
    print(len(decompressed_data))
 
# Decompress file using context manager

with bz2.open('data.bz2', 'rb') as f:
    file_content = f.read()
    print(len(file_content))
 
# Decompress file using context manager

with bz2.
