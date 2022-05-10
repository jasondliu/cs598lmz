from lzma import LZMADecompressor
LZMADecompressor().decompress(COMPRESSED_DATA)

# decompress using zlib
from zlib import decompress
decompress(COMPRESSED_DATA)

# decompress using bz2
from bz2 import decompress
decompress(COMPRESSED_DATA)

# decompress using gzip
from gzip import decompress
decompress(COMPRESSED_DATA)
 
# decompress using lz4
from lz4.frame import decompress
decompress(COMPRESSED_DATA)

# decompress using snappy
import snappy
snappy.decompress(COMPRESSED_DATA)
```

```python
import requests
from bs4 import BeautifulSoup

def get_url_text(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers
