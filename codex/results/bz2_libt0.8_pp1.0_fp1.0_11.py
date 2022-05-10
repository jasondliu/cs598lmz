import bz2
bz2filename = 'sample_file.tar.bz2'

with bz2.open(bz2filename, 'rt') as f:
    data = f.read()

with open('sample_file', 'wt') as f:
    f.write(data)
