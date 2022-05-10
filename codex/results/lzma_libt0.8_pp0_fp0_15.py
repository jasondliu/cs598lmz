import lzma
lzma.decompress(p)

# b'Hello Python!'
```

- `Memoryview`

> 内存视图为文件或字节字符串中的指定字节区域提供了类似数组接口。

```python
>>> s = b"Hello, Python!"
>>> mem = memoryview(s)
>>> mem
<memory at 0x0000020FE72C1600>
>>> mem.tolist()
[72, 101, 108, 108, 111, 44, 32, 80, 121, 116, 104, 111, 110, 33]
>>> mem.readonly
False
>>> mem[3] = 80
>>> s
b'Hello, Pytbon!'
>>> mem = memoryview(s)
>>> mem.tolist()
[72, 101, 108, 108, 111, 44, 32, 80, 121, 116, 104, 111, 110, 33]
>>>
