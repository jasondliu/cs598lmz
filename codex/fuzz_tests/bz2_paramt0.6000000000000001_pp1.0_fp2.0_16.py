from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('/Users/mahbubcseju/Desktop/train-jpg.tar.bz2','rb').read())

import tarfile
tar = tarfile.open("/Users/mahbubcseju/Desktop/train-jpg.tar")
tar.extractall()
tar.close()

import os
os.mkdir('/Users/mahbubcseju/Desktop/train-jpg-sample')
os.mkdir('/Users/mahbubcseju/Desktop/train-jpg-sample/train-jpg')

import shutil
src_dir = "/Users/mahbubcseju/Desktop/train-jpg/"
dst_dir = "/Users/mahbubcseju/Desktop/train-jpg-sample/train-jpg"
for jpgfile in os.listdir(src_dir):
    if jpgfile.endswith(".jpg"):
        shutil.copy(os.path.join(src_dir, jpgfile), dst_dir)

import os
os.mkdir('/Users/mah
