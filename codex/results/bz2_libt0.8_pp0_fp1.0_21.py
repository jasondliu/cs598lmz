import bz2
bz2_file = bz2.BZ2File('example.bz2')
data = bz2_file.read()
bz2_file.close()

data

def bz2_compress(in_file, out_file):
    """Compress a file using bz2 compression."""
    infile = open(in_file, 'rb')
    outfile = bz2.BZ2File(out_file, 'w')
    for line in infile:
        outfile.write(line)
    outfile.close()
    infile.close()

def bz2_decompress(in_file, out_file):
    """Decompress a file using bz2 compression."""
    infile = bz2.BZ2File(in_file, 'r')
    outfile = open(out_file, 'wb')
    for line in infile:
        outfile.write(line)
    outfile.close()
    infile.close()

# bz2_compress('war_and_peace.
