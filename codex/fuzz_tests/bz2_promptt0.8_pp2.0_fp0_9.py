import bz2
# Test BZ2Decompressor
with open('/Users/matthew/Documents/Prog/pythondev/python3/bz2_file.txt', 'rb') as bz2_f:
    bz2_reader = bz2.BZ2Decompressor()
    data = bz2_f.read()
    result = bz2_reader.decompress(data)
print(result)

import zipfile
# Test ZIPFile
test_zip = zipfile.ZipFile('/Users/matthew/Documents/Prog/pythondev/python3/test.zip')
file_in_zip = test_zip.open('test.txt')
for line in file_in_zip.readlines():
    print(line)
