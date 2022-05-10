from lzma import LZMADecompressor
LZMADecompressor().decompress(open('comp_in1.txt').read())

```

```bash
$ python3 ./decompress_lzma.py
```

```
b'j'
```
