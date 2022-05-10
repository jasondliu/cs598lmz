from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%

#import lzma
#lzma.decompress(data)

#%%

import gzip
import json
import io

with io.BytesIO(data) as f:
    with gzip.GzipFile(fileobj=f) as file:
        print(json.load(file))
