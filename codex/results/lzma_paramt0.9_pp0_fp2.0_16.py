from lzma import LZMADecompressor
LZMADecompressor().decompress(open("/tmp/jupyterhub_cookie_secret","rb").read())

# In[ ]:
