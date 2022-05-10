from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('/path/to/file', 'rb').read())
```

```
$ python3 -c "import bz2; print(bz2.decompress(open('/path/to/file', 'rb').read()))"
```

```
$ python3 -c "import bz2; print(bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))"
```

```
$ python3 -c "import bz2; print(bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<
