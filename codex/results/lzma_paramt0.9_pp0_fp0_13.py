from lzma import LZMADecompressor
LZMADecompressor().decompress(_BF)

import pickle
m = pickle.loads(LZMADecompressor().decompress(_BF))
m.r
</code>
It will works :)

