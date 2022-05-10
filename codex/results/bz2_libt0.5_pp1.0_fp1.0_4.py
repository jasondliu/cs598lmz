import bz2
bz2.decompress(compressed_data)

# bz2.compress(data)

f = open('/home/ubuntu/workspace/py/python_for_everyone/files/lines.txt')
f_compressed = bz2.BZ2File('/home/ubuntu/workspace/py/python_for_everyone/files/lines.txt.bz2', 'wb')

for line in f:
    f_compressed.write(line)

f_compressed.close()
f.close()

import gzip

f = gzip.open('/home/ubuntu/workspace/py/python_for_everyone/files/lines.txt.gz', 'wb')
f.write('This is a compress test')
f.close()

f = gzip.open('/home/ubuntu/workspace/py/python_for_everyone/files/lines.txt.gz', 'rb')
file_content = f.read()
f.close()

print file_content

import zipfile

z = zipfile.ZipFile('/
