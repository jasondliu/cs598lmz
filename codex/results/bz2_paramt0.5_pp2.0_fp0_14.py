from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('myfile.bz2').read())

# write to file
with open('myfile.bz2', 'rb') as input:
    with open('myfile.out', 'wb') as output:
        output.write(BZ2Decompressor().decompress(input.read()))

# decompress tar.bz2
from tarfile import open as taropen
taropen('myfile.tar.bz2').extractall()

# decompress gz
from gzip import decompress
decompress(open('myfile.gz').read())

# write to file
with open('myfile.gz', 'rb') as input:
    with open('myfile.out', 'wb') as output:
        output.write(decompress(input.read()))

# decompress tar.gz
from tarfile import open as taropen
taropen('myfile.tar.gz').extractall()

# decompress zip
from zipfile import ZipFile
ZipFile('myfile.zip').extractall()

# decompress
