import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import gzip
gzip.compress(b'Hello World')

import zlib
zlib.compress(b'Hello World')

import zipfile
zipfile.ZipFile('test.zip', 'w').write('test.txt')

import tarfile
tarfile.TarFile('test.tar', 'w').add('test.txt')

import shutil
shutil.copyfile('test.txt', 'test.txt.bak')

import glob
glob.glob('*.py')

import os
os.system('ls -l')

import sys
sys.argv

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

import math
math.cos(math.pi / 4)

import random
random.choice(['apple', 'pear', 'banana'])

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5,
