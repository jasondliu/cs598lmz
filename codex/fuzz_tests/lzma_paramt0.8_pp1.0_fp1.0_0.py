from lzma import LZMADecompressor
LZMADecompressor().decompress(open(sys.argv[1],'rb').read())
```

```
$ python3 lzma_decompress.py ./lzma.out
b'IW{c0mpr3ss1on_1s_n07_s3cur17y}'
```

##### Flag: IW{c0mpr3ss1on_1s_n07_s3cur17y}
