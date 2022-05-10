from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# %%
import lzma
with lzma.open("data/chapter3/sample.xz") as f:
    file_content = f.read()

# %%
import bz2
with bz2.open("data/chapter3/sample.bz2") as f:
    file_content = f.read()

# %%
import gzip
with gzip.open("data/chapter3/sample.gz", "wt") as f:
    f.write(text)

# %%
import gzip
with gzip.open("data/chapter3/sample.gz", "rt") as f:
    text = f.read()

# %%
import gzip
with gzip.open("data/chapter3/sample.gz", "rt") as f:
    for line in f:
        print(line)

# %%
with gzip.open("data/chapter3/sample.gz", "wt") as f:
    f.write(text)

# %%
import gzip
with gzip.open("
