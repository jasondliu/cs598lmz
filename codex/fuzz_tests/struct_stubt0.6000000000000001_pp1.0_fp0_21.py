from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.unpack(b'\x01\x02\x03\x04')
# (16909060,)
```

`Struct` 的构造方法需要一个格式字符串作为参数。格式字符串指明了每个字段的大小和数据类型。支持的格式有：

| Format | C Type             | Python type         | Size | Notes                           |
| ------ | ------------------ | ------------------- | ---- | ------------------------------- |
| x      | pad byte           | no value            |      |                                 |
| c      | char               | bytes of length 1   | 1    |                                 |
| b      | signed char        | integer             | 1    |                                 |
| B      | unsigned char      | integer             | 1    |                                 |
