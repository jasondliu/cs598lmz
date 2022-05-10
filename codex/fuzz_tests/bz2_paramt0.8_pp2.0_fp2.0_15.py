from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open(filename, "rb").read())
 

import gzip
import shutil
with gzip.open('filename.gz', 'rb') as f_in:
    with open('filename', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


from shutil import unpack_archive
unpack_archive('filename.tar')
unpack_archive('filename.tar', 'new_dir')



from bz2 import BZ2File
f = BZ2File('file.bz2', 'r')
file_content = f.read()


import gzip
with gzip.open('data.txt.gz', 'rb') as f:
    file_content = f.read()

import bz2
# TODO: bz2.decompress()
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('file.bz2', "rb").read())



from shutil import unpack_archive
unpack_archive('
