from lzma import LZMADecompressor
LZMADecompressor

# %%
# A class for reading .xz files.  This class inherits from io.BufferedIOBase.

# %%
import lzma

class XZFile(lzma.LZMAFile):
    def __init__(self, filename):
        super().__init__(filename, mode='rt')

# %%
# In Python 3.5, there is an io.TextIOWrapper around the
# LZMAFile internally, which is a subclass of io.BufferedIOBase.

# %%
print(type(XZFile(__file__)))

# %%
# In older versions of Python, there is a io.BufferedIOBase
# wrapper around the LZMAFile.

# %%
print(type(XZFile(__file__)))

# %%
# To read one line at a time:

# %%
for line in XZFile(__file__):
    print(line)

# %%
# The .read() method can be used to read a specified number of bytes,
# and .readinto() can be used to
