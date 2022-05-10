import bz2
bz2.BZ2Compressor()

def bz2_compress(source, destination):
    with open(source, 'rb') as infile:
        with bz2.BZ2File(destination, 'wb') as outfile:
            for line in infile:
                outfile.write(line)
