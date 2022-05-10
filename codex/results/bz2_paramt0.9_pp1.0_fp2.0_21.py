from bz2 import BZ2Decompressor
BZ2Decompressor().decompress()
# import bz2
# bz2.decompress(b'BZh91AY&SY.\xc9\x8e>\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# import gzip
# import shutil
# with gzip.open('data/file.txt.gz', 'rb') as f_in:
#     with open('data/file.txt', 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)

# import gzip, shutil, os
# origfile = 'data/somefile.txt'
# zipfile = 'data/somefile.txt.gz'
#
# # Write to the zip file
# f_in = open(origfile, 'rb')
# f_out = gzip.open(zipfile, 'wb')
# f_out.writelines(f_in
