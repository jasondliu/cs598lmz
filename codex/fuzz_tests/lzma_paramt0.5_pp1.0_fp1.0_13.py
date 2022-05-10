from lzma import LZMADecompressor
LZMADecompressor().decompress(gzip.open('/home/pablo/Downloads/GSE129724_RAW.tar').read()[10:])

import gzip
import io
f = gzip.open('/home/pablo/Downloads/GSE129724_RAW.tar.gz', 'rb')
with open('/home/pablo/Downloads/GSE129724_RAW.tar', 'wb') as outfile:
    outfile.write(f.read())
    
import os
os.listdir('/home/pablo/Downloads/GSE129724_RAW.tar')

import tarfile
tar = tarfile.open('/home/pablo/Downloads/GSE129724_RAW.tar')
tar.getmembers()

import os
os.listdir('/home/pablo/Downloads/GSE129724_RAW/')

import tarfile
tar = tarfile.open('/home/pablo/Downloads/GSE129724_RAW.tar')
for member in tar.getmembers():
    print
