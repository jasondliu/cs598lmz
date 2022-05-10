from lzma import LZMADecompressor
LZMADecompressor().decompress(open('newest32.xml.lzma', 'rb').read())
b'<?xml version="1.0" encoding="utf-8"?>\r\n\r\n<items>\r\n    <item>\r\n        <title>My Feed</title>\r\n    </item\r\n</items>\r\n'
zlib.decompressobj(zlib.MAX_WBITS).decompress(open('newest32.xml.zlib', 'rb').read())
b'<?xml version="1.0" encoding="utf-8"?>\r\n\r\n<items>\r\n    <item>\r\n        <title>My Feed</title>\r\n    </item\r\n</items>\r\n'
```

Similar to the previous example, but uses a stream and compresses directly to the output file.

```python
from lzma import LZMAFile
with LZMAFile('newest32.xml.lzma', 'wb
