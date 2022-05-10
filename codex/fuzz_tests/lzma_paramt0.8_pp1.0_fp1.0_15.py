from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

```
>>> print(LZMADecompressor().decompress(data))
Hello! This is just a test.
```


```
>>> data = open('bla.bla', 'rb').read()
>>> data[:5]
b'%PDF-'
```

```
$ file bla.bla
bla.bla: PDF document, version 1.5
```

```
>>> import zlib
>>> zlib.decompress(data[2:])
b'Hello! This is just a test.'
```

```
>>> import zlib
>>> zlib.decompress(data[2:])
b'Hello! This is just a test.'
```

```
>>> import zlib
>>> zlib.decompress(data[2:])
b'Hello! This is just a test.'
```

```
$ unzip bla.zip
Archive:  bla.zip
  inflating: bla.bla
```

