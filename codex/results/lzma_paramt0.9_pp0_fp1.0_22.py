from lzma import LZMADecompressor
LZMADecompressor().decompress(LZMACompressor().compress(data)).decode()
```

```
$ python3 decompress_lzma.py
flag{so_much_compression}
```

Flag : `flag{so_much_compression}`
