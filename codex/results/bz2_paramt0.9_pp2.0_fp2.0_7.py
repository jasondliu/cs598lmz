from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

bz2_data

bz2_comp = bz2.BZ2Compressor()
bz2_comp.compress(b'message to compress')
bz2_comp.flush()


# Below we see that our bz2.BZ2Decompressor does not work with our BZ2Compressor.
# We get a BZ2File in return and not a byte array like we are used to.
bz2_decomp = bz2.BZ2Decompressor()
bz2_decomp.decompress(bz2_comp.compress(b'message to compress'))


# Working with gzip:
with gzip.open('random_bytes.gz', 'rb') as input:
    with open('random_bytes2.gz', 'wb') as output:
        shutil.copyfileobj(input, output)
        
os.system('file random_bytes2.gz')

os.system('md5sum random_bytes.gz')
os.system('md5sum random
