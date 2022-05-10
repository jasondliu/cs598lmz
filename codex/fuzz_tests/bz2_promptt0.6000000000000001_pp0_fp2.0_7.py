import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
next(bz2_decompressor.decompress(data))

# Test BZ2File
bz2_file = bz2.BZ2File(io.BytesIO(data))
next(bz2_file)

# Test bz2 module functions
bz2.decompress(data)

# Test BZ2Compressor
bz2_compressor = bz2.BZ2Compressor()
bz2_compressor.compress(b'blah')
bz2_compressor.flush()
```

## License

This project is licensed under the [MIT license](LICENSE).
