from lzma import LZMADecompressor
LZMADecompressor().decompress(test)

# %%
with open('test.lzma', 'wb') as fout:
    fout.write(test)

# %%
from lzma import LZMAFile
f = LZMAFile('test.lzma')
f.read()

# %%
f = LZMAFile('test.lzma', 'rb', format=lzma.FORMAT_ALONE)
f.read()

# %%
f = LZMAFile('test.lzma', 'rb', format=lzma.FORMAT_RAW)
f.read()

# %%
f = LZMAFile('test.lzma', 'rb', format=lzma.FORMAT_XZ)
f.read()

# %%
f = LZMAFile('test.lzma', 'rb', filters=lzma.FILTERS_X86)
f.read()

# %%
f = LZMAFile('test.lzma', 'rb', filters=[{'id': lzma.FILTER_
