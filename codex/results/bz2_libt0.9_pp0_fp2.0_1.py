import bz2
bz2_compress_str = bz2.compress(str)

from hashlib import md5
md5_hexdigest_str = md5(str).hexdigest()
```


```python
%%time
for _ in range(10):
    snappy_compress_str
```

    CPU times: user 2 µs, sys: 1 µs, total: 3 µs
    Wall time: 5.96 µs



```python
%%time
for _ in range(10):
    bz2_compress_str
```

    CPU times: user 1 µs, sys: 1e+03 ns, total: 2 µs
    Wall time: 5.01 µs



```python
%%time
for _ in range(10):
    md5_hexdigest_str
```

    CPU times: user 1 µs, sys: 1e+03 ns, total: 2 µs
    Wall time: 5.96 µs


* 개발 맨땅에서 빌
