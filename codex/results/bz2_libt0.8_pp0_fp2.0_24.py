import bz2
bz2.test()

# bz2.BZ2Error: Invalid data stream
# 要解压的文件不是bz2文件

import bz2
file = bz2.BZ2File('/home/shiyanlou/bz2_file.txt.bz2')
file.read()
# b'This is a bz2 compressed file.\n'

file = bz2.BZ2File('/home/shiyanlou/bz2_file.txt.bz2')
file.read(10)
# b'This is a '

with open('/home/shiyanlou/bz2_file.txt', 'wb') as new_file, \
        bz2.BZ2File('/home/shiyanlou/bz2_file.txt.bz2', 'rb') as file:
    for data in iter(lambda: file.read(100 * 1024), b''):
        new_file.write(data)

import bz2
bz
