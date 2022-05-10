from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# Base64
from base64 import b64decode
b64decode(data)

# Standard
'The quick brown fox jumps over the lazy dog'.encode('rot13')

# Hex
from binascii import unhexlify
unhexlify(data)

# ASCII
‘\x34\x32\x37\x37’.decode(‘ascii’)
```

### Problem 13

**Write a script that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically**

**Solution**

```
words = input("Enter a comma separated sequence of words: ").split(',')
words.sort()
print(','.join(words))
```

### Problem 14

**Write a program that accepts a sentence and calculate the number of letters and digits.**

**Solution**

```
s = input('Enter a string: ')
d = {'letters': 0, 'digits': 0}
for char
