import bz2
# Test BZ2Decompressor
bz_decomp = bz2.BZ2Decompressor()
result = bz_decomp.decompress(compressed_data)
result

# Test BZ2File
bz_file = bz2.BZ2File('data/compress_me.bz2')
result = bz_file.read()
result


# ### Exercise 5: Compressing and decompressing streams of data
#
# In this exercise, you'll use the zlib library to compress and decompress streams of text data.

# In[ ]:


import zlib

# Compress a string using zlib

string = b"This is a string that we want to compress"
compressed_string = zlib.compress(string)
compressed_string


# In[ ]:


# Decompress a zlib encoded string

decompressed_string = zlib.decompress(compressed_string)
decompressed_string


# In[ ]:


# Compress a string using gzip

compressed_string = gzip.compress(string
