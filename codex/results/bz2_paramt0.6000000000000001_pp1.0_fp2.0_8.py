from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# Decompress the data with gzip
from gzip import GzipFile
with gzip.GzipFile('data.gz', 'rb') as f:
    data = f.read()

# Open a gzip file for reading
with gzip.GzipFile('data.gz', 'rb') as f:
    data = f.read()

# Open a gzip file for writing
with gzip.GzipFile('data.gz', 'wb') as f:
    f.write(data)

# Read and write compressed data using a buffer
import gzip
import shutil
with gzip.open('data.gz', 'rb') as f_in:
    with open('data', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Read and write compressed data using a buffer
import bz2
import shutil
with bz2.open('data.bz2', 'rb') as f_in:
    with open('data', 'wb') as f_out:
       
