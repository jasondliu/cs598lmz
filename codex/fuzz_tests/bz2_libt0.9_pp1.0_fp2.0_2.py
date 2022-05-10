import bz2
bz2.BZ2Compressor()
```
## bz2文件读取

假设我们现在已经打开了文件，并且创建了一个可用于解压缩的bz2.BZ2Decompressor对象。
要使用它，请使用该decompress()方法。例如：

```
>>> import bz2
>>> un = bz2.BZ2Decompressor()
>>> data = un.decompress(compressed_data)
```

该decompress()方法接受一个字节字符串，并返回可以转换为文本的解压缩字节字符
