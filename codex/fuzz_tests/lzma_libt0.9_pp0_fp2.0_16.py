import lzma
lzma.decompress(b'\xfc\x88\x84\x28\x48\x2f\xd2\x02\x02\x24\x00\x21\x1c\x1c\x07\x57'
b'\x00\x00\x04\x04\x00\x00\x00\x00')

# 7zlib
import lzma
lzma.decompress(b'\x80\x4a\x4f\x4e\x4a')

# MSCompress
import lzma
lzma.decompress(b'\xff\xff\xff\xff\x01')

# MSCompress
import zlib
zlib.decompress(b'\xff\xff\xff\xfb\x00\x14\x01\x00')

# MSCompress
import zlib
zlib.decompress(b'\xff\xff\xff\xfd\x00\x14\x01\x00')
```

