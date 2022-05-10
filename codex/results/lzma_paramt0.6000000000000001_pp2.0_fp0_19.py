from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Decompress data compressed with zlib
from zlib import decompress
decompress(data)
```

The above mentioned compression algorithms are all supported by the Python standard library. You can read more about them [here](https://docs.python.org/3/library/zlib.html).

The data was compressed with a different algorithm than the ones listed above. So, to decompress the data, you need to use an external library named `lz4`:

```
pip install lz4
```

Once you have installed the library, you can decompress the data as follows:

```
from lz4.block import decompress
decompress(data)
```

This gives you the flag.

## Flag

`picoCTF{compressi0n_is_in_3verything_33d2f30c}`
