from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# output: b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
```

_Another way_ is to, instead of decompressing the whole file, we will use [`bz2.BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File) class, which acts like a regular file and produces chunks of data on demand, as we iterate over the file.

This will save us some memory:

```python
import bz2

data = None
with bz2.BZ2File('large_file.bz2') as f:
    for line in f:
        data = line
        print(line)

# output: b'The first line\n'
```

Due to the fact, that
