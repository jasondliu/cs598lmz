import bz2
bz2.BZ2File(fname)

# compress_level: [1, 9]
with bz2.BZ2File(fname_bz2, 'wb', compresslevel=9) as f:
    f.write(b'hello world!')

with bz2.BZ2File(fname_bz2) as f:
    print(f.read())

import lzma
fname_xz = fname + '.xz'
with lzma.LZMAFile(fname_xz, 'w') as f:
    f.write(b'hello world!')

with lzma.LZMAFile(fname_xz) as f:
    print(f.read())

import shutil
shutil.make_archive('archive', 'zip', root_dir='./')
shutil.unpack_archive('archive.zip')

# copy mode: copy2
import os
os.chmod(fname, 0o444)
shutil.copy(fname, fname_copy)
shutil
