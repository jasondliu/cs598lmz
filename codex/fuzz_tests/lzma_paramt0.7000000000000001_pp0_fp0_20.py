from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

## Block

每个块都由头和数据组成，头有固定大小（4K）数据可以是任意大小。

```
+------------+------+----------+
|    header  | data | padding  |
+------------+------+----------+
```

## Header

头部固定大小（4K）。整个文件可以被分割为可以由2^n个块组成，n>=0，每个块表示一个压缩等级。

```
+----------------------+----------+-------+
|      field size      |  field   | value |
+----------------------+----------+-------+
|
