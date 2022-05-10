from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)

# Create the data structure you want to build
data = {
    "person": {
        "name": "Bob",
        "languages": ["English", "Fench"],
        "married": True,
        "age": 32
    }
}

# Write out the data
with bz2.BZ2File('data.json.bz2', 'w') as f:
    json.dump(data, f)

# Read the data back in
with bz2.BZ2File('data.json.bz2', 'r') as f:
    data_loaded = json.load(f)

from bz2 import BZ2Compressor
c = BZ2Compressor()
c.compress(b"some data")
c.flush()

# Compress data incrementally
from bz2 import BZ2Compressor
from functools import partial

compressor = BZ2Compressor()
compress = partial(compressor.compress, b"some data")

import bz2

# Comp
