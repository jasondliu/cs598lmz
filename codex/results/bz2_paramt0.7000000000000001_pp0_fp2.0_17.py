from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(m)

# Out: b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
```

Let's try the same with `lzma`:

```python
import lzma
lzma.decompress(m)

# Out: b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
```

Both work, but the BZ2 decoder is faster, so we'll stick with that.

##### decompressor_name

The name of the compressor used.

```python
from bz2 import decompress
from dill.source
