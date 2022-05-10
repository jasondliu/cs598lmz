import bz2
# Test BZ2Decompressor
# https://stackoverflow.com/questions/3288595/how-to-decompress-a-bzipped-string-in-python

compdata = open('data/compdata.bz2', 'rb')

decomper = bz2.BZ2Decompressor()
data = decomper.decompress(compdata.read())

print(data)

compdata.close()

# Test BZ2Compressor

data = b'This is the original text.'

comper = bz2.BZ2Compressor()
compdata = comper.compress(data) + comper.flush()

print(compdata)

open('data/compdata.bz2', 'wb').write(compdata)

# Test compressing and decompressing data

data = b'This is the original text.'

comper = bz2.BZ2Compressor()
compdata = comper.compress(data) + comper.flush()

decomper = bz2.BZ2Decompressor()
data
