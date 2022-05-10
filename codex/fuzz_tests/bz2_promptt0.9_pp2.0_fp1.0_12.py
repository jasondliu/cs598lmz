import bz2
# Test BZ2Decompressor

data = bz2.BZ2File('../asset/mystery.bz2')
decompressor = bz2.BZ2Decompressor()

try:
    for block in iter(lambda : data.read(100 * 1024), b''):
        print(decompressor.decompress(block))
except EOFError:
    print(decompressor.flush())

print(decompressor.unused_data)

print('Done')

#

 
#

#
 
#

 
#

#
 
#

#
 
#

#
 
#

#
 
#

#
 
#

#
 
#

#
 
#

#
 
#

#
 
#

 
#

 
#

#
 
#

#
 
#

#
 
#

#
 
#

#
 
#

#
 
#

#
 
#

#
 
