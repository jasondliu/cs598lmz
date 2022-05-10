import bz2
# Test BZ2Decompressor

with bz2.BZ2File('../data/sample.bz2', 'r') as f:
    file_content = f.read()
    print(file_content)

# Test BZ2Compressor

data = b'This is the data to compress.'

with bz2.BZ2File('../data/sample.bz2', 'w') as f:
    f.write(data)
 
# Test BZ2File

with bz2.BZ2File('../data/sample.bz2', 'r') as f:
    file_content = f.read()
    print(file_content)
 
# Test BZ2File

data = b'This is the data to compress.'

with bz2.BZ2File('../data/sample.bz2', 'w') as f:
    f.write(data)
 
# Test BZ2File

with bz2.BZ2File('../data/sample.bz2', 'r') as f:
    file_content = f
