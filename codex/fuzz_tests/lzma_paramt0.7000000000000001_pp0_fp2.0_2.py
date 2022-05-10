from lzma import LZMADecompressor
LZMADecompressor().decompress(resp.content)

# %% [markdown]
# ### bz2
# [bz2 — Support for bzip2 compression](https://docs.python.org/3/library/bz2.html)

# %%
from bz2 import decompress
decompress(resp.content)

# %% [markdown]
# ### zlib
# [zlib — Compression compatible with gzip](https://docs.python.org/3/library/zlib.html)

# %%
from zlib import decompress
decompress(resp.content)
