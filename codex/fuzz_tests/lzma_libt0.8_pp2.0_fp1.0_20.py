import lzma
lzma.LZMADecompressor().decompress(data)

```       
```
$ python3 18.py 
b'I am LZMA compressed!'
```

### 19 - Implement RSA
```
https://www.nostarch.com/crackingcodes/ (BSD Licensed)
```

```
>>> from Crypto.Util.number import *
>>> p = getPrime(512)
>>> q = getPrime(512)
>>> n = p * q
>>> phi = (p - 1) * (q - 1)
>>> e = 65537
>>> d = inverse(e, phi)
>>> p, q, e, d
(10472290276622496140193877130107520992370957336928857039091278996808058773943546627773515271309126801625148601981004877944444445967589805556509866258557224362600595051038975377837474851724192858459992155
