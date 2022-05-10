import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('sample.tar.bz2', 'rb') as f:
    file_content = f.read()

uncompressed_data = bz2_decompressor.decompress(file_content)
uncompressed_data

# Test BZ2File

with bz2.BZ2File('sample.tar.bz2', 'rb') as f:
    file_content = f.read()

file_content

# Test TarFile

import tarfile

with tarfile.open('sample.tar.bz2', 'r:bz2') as tar:
    for member_info in tar.getmembers():
        print(member_info.name)
        f = tar.extractfile(member_info)
        print(f.read())
 
# Test BZ2File

with bz2.BZ2File('sample.tar.bz2', 'rb') as f:
    file_content = f.read()

