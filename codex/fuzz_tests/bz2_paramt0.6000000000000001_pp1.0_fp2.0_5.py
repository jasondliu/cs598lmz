from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

def bz2_read(filename):
    return BZ2Decompressor().decompress(open(filename, 'rb').read())

def bz2_write(filename, data):
    open(filename, 'wb').write(BZ2Decompressor().compress(data))

def bz2_append(filename, data):
    open(filename, 'ab').write(BZ2Decompressor().compress(data))

print(bz2_read('lorem.txt.bz2'))
