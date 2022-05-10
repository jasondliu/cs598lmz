from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)
```

```
b'This is the original text.'
```

如果在上面的例子中，压缩文件是很大的，那么可以使用`BZ2Decompressor`类的`decompress()`方法来推进解压过程。

```python
from bz2 import BZ2Decompressor

# Get a file-like object for the Python Web site's home page.
import urllib.request
response = urllib.request.urlopen('http://www.python.org')
compressed_data = response.read()

# Wrap the compressed data in a BZ2Decompressor object
decompressor = BZ2Decompressor()

# Decompress the data
data = decompressor.decompress(compressed_data)

# Check if the end of data has been reached
print(dec
