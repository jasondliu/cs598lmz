import bz2
bz2.BZ2File

# if we have a file handle, we can use it to open a bz2 file

bz2_file = bz2.BZ2File(fileobj=file_handle)
bz2_file

# in this case, we can use a context manager to open the file
with bz2.BZ2File('data/example.json.bz2') as bz2_file:
    for line in bz2_file:
        print(line.strip())
# if we want to open a gzip file, we can use gzip.GzipFile

import gzip
gzip.GzipFile

# if we have a file handle, we can use it to open a gz file

gz_file = gzip.GzipFile(fileobj=file_handle)
gz_file

# in this case, we can use a context manager to open the file
with gzip.GzipFile('data/example.json.gz') as gz_file:
    for line in gz_file:
        print(line.strip())
