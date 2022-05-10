import bz2
bz2.decompress(compressed)

#encoded_text = bz2.compress(text)
#print encoded_text

#bz2.decompress(encoded_text) -> True
#    print(bz2.decompress(encoded_text))
import os
os.listdir('sample_data/')

import tarfile
os.chdir(os.getcwd()+'/sample_data')
os.listdir(os.getcwd())

with tarfile.open('archive.tar.bz2', "r:bz2") as tar:
    tar.extractall()

os.listdir('.')

import shutil
#make archive, -9 is max compresion
shutil.make_archive('archive', 'bztar', root_dir='.')
os.listdir('.')

#if we created another archive
shutil.make_archive('archive2', 'bztar', root_dir='.')
os.listdir('.')

##################
#GZ
shutil.
