from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# In[ ]:


# gzip
import gzip
s = b'witch which has which witches wrist watch'
len(s)
t = gzip.compress(s)
len(t)
gzip.decompress(t)

# In[ ]:


# bz2
import bz2
s = b'witch which has which witches wrist watch'
len(s)
t = bz2.compress(s)
len(t)
bz2.decompress(t)

# In[ ]:


# contextlib
from contextlib import contextmanager
@contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')

