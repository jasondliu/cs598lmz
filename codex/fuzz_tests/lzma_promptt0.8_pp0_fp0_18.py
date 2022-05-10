import lzma
# Test LZMADecompressor().
decoder = lzma.LZMADecompressor()
f = open('./pydata-book-master.tar.xz', 'rb')
data = f.read(10)
f.close()
data

# In[5]:


decoded = decoder.decompress(data)
decoded

# In[6]:


decoder = lzma.LZMADecompressor()
f = open('./pydata-book-master.tar.xz', 'rb')
with open('outfile.tar', 'wb') as outfile:    
    while True:
        buf = f.read(1024)
        if not buf:
            break
        outfile.write(decoder.decompress(buf))
f.close()

# In[7]:


with open('outfile.tar', 'rb') as f:
    data = f.read()
data

# In[8]:


with open('./examples/ex1.csv') as f:
    data = list(csv.reader
