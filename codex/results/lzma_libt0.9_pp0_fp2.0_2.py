import lzma
lzmaObj=lzma.LZMAFile('data.py',"w",options=lzma.FORMAT_RAW)
lzmaObj.write(data)
lzmaObj.close()

del data
del lzmaObj

fileObj = open('data.py',"rb")
lzmaObj = lzma.open('lzma_data.py',"w",options=lzma.FORMAT_RAW)

while 1:
    data = fileObj.read(4096)
    if not data:
        break
    lzmaObj.write(data)
lzmaObj.close()
fileObj.close()
import lzma
fileObj = open('data.py',"rb")
lzmaObj = lzma.open('lzma_data.py',"w")
while 1:
    data = fileObj.read(4096)
    if not data:
        break
    lzmaObj.write(data)
lzmaObj.close()
fileObj.close()

import bz2

bz2obj
