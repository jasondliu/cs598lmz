from lzma import LZMADecompressor
LZMADecompressor().decompress(open("phile.txt.xz", "rb").read()).decode()

# lzmaffi 0.21.1 has a depricated msg, but same result.
import lzmaffi
lzmaffi.decompress(open("phile.txt.xz", "rb").read()).decode()

# xz 2.0.1, throw an error.
# ImportError: xz library not found. Please install the liblzma-dev package.
import xz
xz.decompress(open("phile.txt.xz", "rb").read()).decode()

# Error caught by pyxz (Python 3.8.3)
import pyxz
pyxz.decompress(open("phile.txt.xz", "rb").read()).decode()
