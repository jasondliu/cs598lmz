from bz2 import BZ2Decompressor
BZ2Decompressor()


# In[3]:


try:
    from lzma import LZMADecompressor
    LZMADecompressor()
except ImportError:
    # Aged Python, you have an LZMA module, but no LZMADecompressor
    # Let's monkey-patch LZMADecompressor in
    import lzma
    lzma.LZMADe
