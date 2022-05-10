import bz2
bz2.BZ2File(file_name)

import gzip
gzip.open(file_name, 'rt')

import lzma
lzma.open(file_name)

import zipfile
with zipfile.ZipFile(file_name) as f:
    f.read('README')

with tarfile.open(file_name) as f:
    f.extractall(path='/tmp')

import shutil
with gzip.open('file_name.gz', 'rb') as f_in:
    with open('file_name', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

shutil.unpack_archive('file_name.tar.gz', extract_dir='/tmp/')

shutil.make_archive('archive_name', 'zip', root_dir='/tmp/')

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

re.sub(r'(\b[a-z
