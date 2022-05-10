import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

# decompress data from a text file

# store decompressed data
data = []

with bz2.BZ2File('./data/compressed.bz2', 'rb') as f:
    # get the decompressed data
    for block in iter(lambda: f.read(100 * 1024), b''):
        data.append(decompressor.decompress(block))

# join the list into a single byte string
data = b''.join(data)

# decode byte string into string
text = data.decode('utf-8')

# display first 2000 characters
print(text[:2000])


# ### Using the BZ2File

# In[5]:

# import bz2
import bz2
# Test BZ2Decompressor
# decompressor = bz2.BZ2Decompressor()

# decompress data from a text file
# store decompressed data
data = []

with bz2.BZ2File('./data/comp
