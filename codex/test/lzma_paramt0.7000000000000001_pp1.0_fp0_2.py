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
