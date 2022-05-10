import bz2
bz2_file = bz2.BZ2File('data/sample.bz2')
bz2_file.read()

import gzip
gzip_file = gzip.open('data/sample.gz')
gzip_file.read()

import zipfile
zip_file = zipfile.ZipFile('data/sample.zip')
zip_file.extractall('data/sample')
zip_file.close()

import tarfile
tar_file = tarfile.open('data/sample.tar')
tar_file.extractall('data/sample')
tar_file.close()

import glob
glob.glob('data/sample/*')

import os
os.remove('data/sample/sample.txt')
os.rmdir('data/sample')

#%%
# 텍스트 파일 읽고 쓰기

with open('data/sample.txt', 'r') as f:
    text = f.read()

with open('data/sample.txt
