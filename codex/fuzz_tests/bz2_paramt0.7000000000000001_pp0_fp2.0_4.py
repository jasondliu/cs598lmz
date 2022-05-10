from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('data/' + str(fn)+'_bz2').read())

# In[ ]:
