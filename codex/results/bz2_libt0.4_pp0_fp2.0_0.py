import bz2
bz2.decompress(bz2_data)

# Compress a file
with open('data/file.txt', 'rt') as input:
    with bz2.open('data/file.txt.bz2', 'wt') as output:
        for line in input:
            output.write(line)

# Decompress a file
with bz2.open('data/file.txt.bz2', 'rt') as input:
    with open('data/file_copy.txt', 'wt') as output:
        for line in input:
            output.write(line)

# Compress a file using command line
# bzip2 data/file.txt
# bzip2 -d data/file.txt.bz2
