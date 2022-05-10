from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(E_read('BZ2-impls.tar.bz2'))

################################################################################

### Drifting around in a BZ2 compressed blob from a JPG image
JPG = 'MOOCULUS-LOGO.jpg'

###
##### Here are our native Python implementations of the two 
##### algorithms for compressing and decompressing BZ2 files:

def bz2_compresses(s):
    return BZ2Compressor().compress(s) + BZ2Compressor().flush()

def bz2_decompresses(s):
    return BZ2Decompressor().decompress(s) + BZ2Decompressor().flush()

###
###### When we apply our compression function to the raw bytes data
###### of the JPG image, the result is a compressed blob:

print(len(E_read(JPG)) == len(bz2_compresses(E_read(JPG))))   # True

###
###### This is the correct length; our compression functions are
###### doing blobs with no
