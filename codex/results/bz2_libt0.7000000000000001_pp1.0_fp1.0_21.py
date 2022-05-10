import bz2
bz2.decompress(data)

def write_to_bz2_file(data, filepath):
    """ Write binary data to a file compressed with bzip2. """
    with bz2.BZ2File(filepath, 'w') as f:
        f.write(data)


def read_from_bz2_file(filepath):
    """ Read binary data from a file compressed with bzip2. """
    with bz2.BZ2File(filepath, 'r') as f:
        data = f.read()
    return data

import os
filepath = os.path.join(os.getcwd(), 'data.bz2')

write_to_bz2_file(data, filepath)
read_from_bz2_file(filepath)

#%%

import gzip

def write_to_gzip_file(data, filepath):
    """ Write binary data to a file compressed with gzip. """
    with gzip.GzipFile(filepath, 'wb') as f:
       
