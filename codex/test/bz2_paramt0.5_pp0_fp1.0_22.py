from bz2 import BZ2Decompressor
BZ2Decompressor()

import gzip
import shutil

def uncompress(source_filepath, dest_filepath, block_size=65536):
    with gzip.open(source_filepath, 'rb') as s_file, open(dest_filepath, 'wb') as d_file:
        shutil.copyfileobj(s_file, d_file, block_size)

def decompress(source_filepath, dest_filepath, block_size=65536):
    with bz2.BZ2File(source_filepath, 'rb') as s_file, open(dest_filepath, 'wb') as d_file:
        shutil.copyfileobj(s_file, d_file, block_size)

def extract_tar(source_filepath, dest_filepath, tar_type='gz'):
    if tar_type == 'gz':
        tar = tarfile.open(source_filepath, "r:gz")
