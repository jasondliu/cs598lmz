import bz2
bz2.BZ2File(filename, 'w')

# Open a gzip-compressed file in binary write mode
import gzip
gzip.open(filename, 'wb')

# Open a bz2-compressed file in binary write mode
import bz2
bz2.BZ2File(filename, 'wb')

# Read & write data in binary mode
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

# Read binary data from a file
with open('somefile.bin', 'rb') as f:
    data = f.read()

# Write binary data to a file
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')

# Read the entire file as a single byte string
with open('somefile.bin', 'rb
