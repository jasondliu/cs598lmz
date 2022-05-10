import bz2
# Test BZ2Decompressor

source = 'Hello world! I am 9 characters long.'

compressor = bz2.BZ2Compressor()
compressed = compressor.compress(source)
compressed += compressor.flush()

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(compressed)

print 'Source     :', len(source), repr(source)
print 'Compressed :', len(compressed), repr(compressed)
print 'Decompressed:', len(decompressed), repr(decompressed)


# In[11]:


# Test BZ2File

source = 'Hello world! I am 9 characters long.'

fout = bz2.BZ2File('out.bz2', 'w')
fout.write(source)

with open('source.txt', 'w') as sourcefile:
    sourcefile.write(source)

get_ipython().magic(u'ls *')


# In[12]:


import tarfile
with tarfile.open('example.tar') as
