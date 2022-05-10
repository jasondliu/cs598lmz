import bz2
# Test BZ2Decompressor:
d = bz2.BZ2Decompressor()
d

# In[2]:

blob = open("blob.bz2", "rb").read()
blob_decompressed = d.decompress(blob)
# Now, blob_decompressed is a string!
blob_decompressed


# In[3]:

# Test BZ2Compressor:
d = bz2.BZ2Compressor()
d

# In[4]:

# Let's try some compression of two interleaved letters:
c = d.compress("a") # "a" is the first character to be compressed.
c = d.compress("b") # "b" is the second character to be compressed.
c = d.flush() # Flushing the compressor returns the rest of the bytes.
c
# c has the following structure:
# c = bytes(0xc0) + <sequence_length> + <sequence> + bytes(0x17) + <sequence_length> + <sequence> + EOF


# In[5]:


