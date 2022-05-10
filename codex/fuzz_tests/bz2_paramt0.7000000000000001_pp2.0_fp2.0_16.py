from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(bz2.decompress(data)))[:5]

# get the data, first delete the header (those are the bytes you get from 
# the first bz2.decompress), then feed it to the second bz2 decompressor

data2 = data.split(b'\x1f\x8b\x08\x00\x00\x00\x00\x00')[1]
BZ2Decompressor().decompress(data2)[:5]
```

### Get the data, then decode from bytes to string, then show a random word
```python
# feed the data to the first bz2 decompressor, then get the string
text = BZ2Decompressor().decompress(data).decode("utf-8")

# split the string into words, and get a random word
words = text.split()
random.choice(words)
```

### Get the data and some words from it
```python
# feed the data to the first bz2 decompressor,
