import lzma
lzma.open('input.txt.xz')

# gzip
import gzip
gzip.open('input.txt.gz')

# bz2
import bz2
bz2.open('input.txt.bz2')

# zip file
import zipfile
zipfile.ZipFile('input.zip') # zipfile.ZipFile('input.zip', 'r')

# tar file
import tarfile
tarfile.open('input.tar') # tarfile.open('input.tar', 'r')

# file system
import pathlib
pathlib.Path('input.txt')

# file system
import os
os.path.isfile('input.txt')
os.path.isdir('input.txt')
os.path.exists('input.txt')
os.path.getsize('input.txt')
os.path.getmtime('input.txt')
os.listdir('.')
os.mkdir('./tmp')
os.rmdir('./tmp')

# file system
import shutil
shutil.copy
