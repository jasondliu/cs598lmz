from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# decompress from file

with open("test_file.lzma", "rb") as input_file:
  data = input_file.read()

with LZMADecompressor() as decompressor:
  decompressed_data = decompressor.decompress(data)

# decompress multiple data blocks

with LZMADecompressor() as decompressor:
  data = b"some data"
  while True:
    chunk = decompressor.decompress(data)
    if chunk:
      print(chunk)
    else:
      break
```

## License

This project is licensed under the [MIT license](https://github.com/python/cpython/blob/3.7/LICENSE).

## Links

- [Documentation](https://docs.python.org/3/library/lzma.html)
- [Source code](https://github.com/python/cpython/tree/3.7/Lib/lzma.py)
- [Issue tracker](https://bugs.
