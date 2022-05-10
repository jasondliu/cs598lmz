from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

'''
http://www.bz2file.org/
bz2file is a Python library for reading and writing bzip2-compressed files.
For file objects, a convenience class that wraps compression and decompression
'''

import bz2
fileopen = bz2.BZ2File('myfile.bz2')
content = fileopen.read()
print(content)

fileopen = bz2.BZ2File('myfile.bz2','wb')
fileopen.write(b'This is a test')
fileopen.close()

fileopen = bz2.BZ2File('myfile.bz2')
print(fileopen.readline() == b'This is a test')

fileopen.read()

'''
    all compressed file objects provide:
    read
    readline
    readlines
    writelines
    __iter__
    close
    tell
    seek
'''
