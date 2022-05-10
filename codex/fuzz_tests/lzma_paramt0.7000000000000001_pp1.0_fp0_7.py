from lzma import LZMADecompressor
LZMADecompressor.decompress(b'\x00\x10\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14')
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.7/lzma.py", line 1028, in decompress
    self._buffer.extend(self._decompressor.decompress(data, max_length))
  File "/usr/lib/python3.7/lzma.py", line 899, in decompress
    return self._buffer.read() + result
  File "/usr/lib/python3.7/lzma.py", line 767, in read
    raise EOFError("Compressed file ended before the "
EOFError: Compressed file ended before the end-of-stream marker was reached
