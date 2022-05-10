import bz2
bz2_file = bz2.BZ2File('test.xml.bz2', 'w')
bz2_file.write(data)
bz2_file.close()
# Read the file by chunk
bz2_file = bz2.BZ2File('test.xml.bz2', 'r')
chunk = bz2_file.read(10)
chunk

# Read the file line by line
bz2_file.readline()
bz2_file.readline()
bz2_file.readline()
bz2_file.readline()

# Iterate over the file
for line in bz2_file:
    print(line)

# Close file
bz2_file.close()
from bz2 import compress, decompress
data = 'bz2 compress'.encode('utf-8')
compressed = compress(data)
compressed
decompressed = decompress(compressed)
decompressed
decompressed.decode('utf-8')
 
import os
os.path.
