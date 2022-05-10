from lzma import LZMADecompressor
LZMADecompressor().decompress(_meta[b'index'][b'lzma_blob'])

```

```
# BSON file
Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from bson import decode_file_iter
>>> for i in decode_file_iter(_meta[b'db_file']):
...    print(i)
...
{'_id': ObjectId('5b95fe717a9f36d6751c2e1e'), 'name': 'John Doe'}
{'_id': ObjectId('5b95fe917a9f36d6751c2e28'), 'name': 'John Doe'}
{'_id': ObjectId('5b95fe967a9f36d6751c2e
