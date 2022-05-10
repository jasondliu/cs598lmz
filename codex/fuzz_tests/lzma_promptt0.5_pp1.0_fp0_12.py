import lzma
# Test LZMADecompressor with a file-like object
with open('lzma_compressed_file', 'rb') as input, \
     lzma.open('lzma_decompressed_file', 'wb',
               format=lzma.FORMAT_XZ,
               check=-1,
               preset=9,
               filters=[
                   {"id": lzma.FILTER_LZMA1,
                    "dict_size": 2 ** 23,
                    "lc": 3,
                    "lp": 0,
                    "pb": 2,
                    "mode": lzma.MODE_NORMAL,
                    "nice_len": 128,
                    "mf": lzma.MF_HC4,
                    "depth": 0}]) as output:
    output.write(input.read())
```

## 参考

- [Python3 压缩与解压缩](https://www.cnblogs.com/zhaof/p/python3_compress_and_decompress.html)
- [python 压缩
