import lzma
lzma.decompressobj()
```

```
>>> import lzma
>>> import os
>>> file_name = "lookup.dat"
>>> file_size = os.path.getsize(file_name)
```

```python
>>> import pickle
>>> with open(file_name, mode='rb') as file: # b is important -> binary
...      fileContent = file.read()
>>> data = pickle.loads(fileContent)
>>> o = data
```

A lot of data. Let's see what we're dealing with:

```python
>>> o.keys()
dict_keys(['ab', 'af', 'ar', 'bg', 'bn', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'ga', 'gl', 'gu', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'iw', 'ja', 'ka', 'kn', 'ko
