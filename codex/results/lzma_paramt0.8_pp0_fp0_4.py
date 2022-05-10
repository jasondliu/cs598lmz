from lzma import LZMADecompressor
LZMADecompressor().decompress(compresseddata)
```

```
$ time python3 uncompressor.py
Hello World!

real    0m0.011s
user    0m0.009s
sys     0m0.002s
```

## Compress Text Files

```
$ cat file.txt
Hello World!
```

```
$ python3 compresstextfile.py file.txt
b'\xfd7\xcb\xc8\x00\x03\x04\x01\x00 \x00\xf4H\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00!\x9c\x04\xd1,\x00\x00\x00'
```

```
$ python3 decompresstextfile.py compressedfile.txt.xz
Hello World!
```

```
$ time python3 decompresstextfile.py compressedfile.txt.xz
Hello World!

real    0m0.018s
user    0
