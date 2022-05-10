import bz2
bz2.open(datafile)

# Write compressed data to a file - appends .bz2 to file's name
with bz2.open('compressed.txt.bz2', 'wt') as f:
    f.write('Contents go here!')

# Inspect compression ratio
import os
original_size = os.path.getsize('data.txt')
compressed_size = os.path.getsize('compressed.txt.bz2')

print('original_size is {} bytes'.format(original_size))
print('compressed_size is {} bytes'.format(compressed_size))
print('compression ratio is {}'.format(original_size/compressed_size))


# Zip
# Import modules
import zipfile
from zipfile import ZipFile

# Create and open zip files in read mode
with ZipFile('files.zip', 'r') as zip:
    # List all contents of the zip file
    zip.namelist()

    # Extract all contents from the zip file
    zip.extractall()

    # Extract a specific file
    zip.extract
