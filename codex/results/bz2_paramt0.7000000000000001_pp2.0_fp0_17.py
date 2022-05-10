from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# Run
# python -m bz2 -d sample.txt.bz2
# to decompress the file

# Another way is to use the shutil module
import shutil
with open('sample.txt', 'rb') as input, open('sample.txt.bz2', 'wb') as output:
    shutil.copyfileobj(input, output)

# To create a tar.gz file
import tarfile
with tarfile.open('sampleDir.tar.gz', 'w:gz') as tr:
    tr.add('sampleDir')

# To extract a tar.gz file
import tarfile
with tarfile.open('sampleDir.tar.gz') as tr:
    tr.extractall()
