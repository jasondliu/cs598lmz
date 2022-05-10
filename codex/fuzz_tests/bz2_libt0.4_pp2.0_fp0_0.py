import bz2
bz2.BZ2File(filename, 'wb', compresslevel=9)

# Compress data iteratively
import bz2
compressor = bz2.BZ2Compressor(9)
with open('file.txt.bz2', 'wb') as f:
    for data in iter(lambda : f.read(100), b''):
        f.write(compressor.compress(data))
    f.write(compressor.flush())

# Decompress data
import bz2
with bz2.open('file.txt.bz2', 'rb') as f:
    data = f.read()

# Compress data using context manager
import bz2
with bz2.open('file.txt.bz2', 'wb') as f:
    f.write(b'Hello World')

# Decompress data using context manager
import bz2
with bz2.open('file.txt.bz2', 'rb') as f:
    print(f.read())

# Compress data using context manager
import bz2

