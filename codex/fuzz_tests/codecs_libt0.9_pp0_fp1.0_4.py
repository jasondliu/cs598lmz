import codecs
codecs.register_error("strict", codecs.ignore_errors)
```

``` Python
f = codecs.open("input.txt", "r", "latin-1")
for line in f:
    line.encode("utf-8")
f.close()
```

### 7.4.4의 unicodedata 모듈

``` Python
import unicodedata
u = "caf\u00e9"
p = "".join(chr(char) for char in u.encode("utf-8"))
unicodedata.normalize("NFC", p)
```

## 7.5 날짜와 시간

> 파이썬1에서는 어떤 일이 발생하였는지를 파악하기 위해 일을 하는 사
