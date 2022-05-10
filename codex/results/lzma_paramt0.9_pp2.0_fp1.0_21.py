from lzma import LZMADecompressor
LZMADecompressor.decompress(b''.join(data)).decode()

# same result, but woah it's slower


# #### Alternate (mike)

# In[ ]:


b''.join(data).decode('lzma')


# #### Another (mike)

# In[ ]:


import lzma
import sys
infile = sys.stdin.buffer.raw
outfile = sys.stdout.buffer
dec = lzma.LZMADecompressor()
data = b''
for s in iter(lambda: infile.read1(4096), b""):
    data += dec.decompress(s)
    if not s:
        break 
print(data)


# #### Using `python-lzma` directly

# In[ ]:


import lzma
LZMADecompressor(data).decompress().decode()

# fails


# #### Streaming the data over a pipe

# In[ ]:


from subprocess import Popen, PIPE
with Popen
