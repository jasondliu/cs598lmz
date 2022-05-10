import bz2
bz2_file = bz2.open('test_data_bzip2.bz2', 'rb')
bz2_file.seek(-10, 2)
bz2_file.read(10)

#10.2.2.3. gzip and bz2 Module Limitations
#10.2.3. Reading Compressed Files in Chunks
bz2_file = bz2.open('test_data_bzip2.bz2', 'rb')
while True:
    chunk = bz2_file.read(100)
    if len(chunk) == 0:
        break
    process_data(chunk)

#10.3. The zlib Compression Algorithm
#10.3.1. zlib Compression
import zlib
s = b'witch which has which witches wrist watch'
len(s)
#37
t = zlib.compress(s)
len(t)
#25
zlib.decompress(t)
#b'witch which has which witches wrist watch'
zlib.crc32(s)

