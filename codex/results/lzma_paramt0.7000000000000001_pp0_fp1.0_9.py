from lzma import LZMADecompressor
LZMADecompressor().decompress(data_lzma)

# bzip2
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data_bzip2)

# zlib
import zlib
zlib.decompress(data_zlib)
```


```
# gzip
import gzip
with gzip.open('example.gz', 'rb') as f:
	f.read()
```


# Miscellaneous
## `requests`
https://realpython.com/python-requests/
```
import requests

# Get
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()

# Post
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r.text

# Upload files
url = 'http://httpbin.org/post'
files = {'file
