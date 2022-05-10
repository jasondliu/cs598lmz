import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
bz2_data = bz2.compress(s)
uncompressed_data = decompressor.decompress(bz2_data)
uncompressed_data

# In[ ]:
#################################################################################################
import zlib
# Test zlib decompressor
zlib_data = zlib.compress(s)
unzlib_data = zlib.decompress(zlib_data)
while unzlib_data[-1] == 'Z':
    unzlib_data = unzlib_data[:-1]
# Seems to be the same! Also as expected
unzlib_data

# In[ ]:
#################################################################################################
# Test bz2 decompressor
bz2_decompressor = bz2.BZ2Decompressor()
raw_bz2_data = open('address.xml.bz2').read()
edata = bz2_decompressor.decompress(raw_bz2_data)
decompressed_data = z
