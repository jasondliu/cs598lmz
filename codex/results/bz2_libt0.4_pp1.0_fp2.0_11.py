import bz2
bz2.BZ2File(path, 'rb')

# read the entire file into a Python array
with bz2.BZ2File(path, 'rb') as f:
    data = f.read()

# decompress the data
data = bz2.decompress(data)

# write a compressed file
with bz2.BZ2File('/mnt/data/file.bz2', 'wb') as f:
    f.write(data)

# read from a compressed file directly into a buffer
buf = bytearray(100_000_000)
with bz2.BZ2File('/mnt/data/file.bz2', 'rb') as f:
    n = f.readinto(buf)

buf[:n]

# compress data incrementally
import bz2
compressor = bz2.BZ2Compressor()
with open('/mnt/data/file.json', 'rb') as input:
    with open('/mnt/data/file.json.bz2', 'wb') as
