import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressed_data = decompressor.decompress(compressed_data)

# Test LZMAFile
with lzma.open('file.xz', 'rt') as f:
    text = f.read()

# Test LZMAError
try:
    decompressor.decompress(b'Malformed data')
except lzma.LZMAError as e:
    print('Error:', e)

# Test compress
with open('file.xz', 'wb') as f:
    f.write(compressed_data)

# Test compressfile
with open('file.txt', 'rt') as f_in, lzma.open('file.txt.xz', 'wt') as f_out:
    f_out.writelines(f_in)
```

```
$ python lzma.py
Error: LZMAError: Error in data stream
```

## xz (XZ Utils)

```
$ xz --
