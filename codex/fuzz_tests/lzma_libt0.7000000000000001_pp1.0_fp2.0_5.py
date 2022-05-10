import lzma
lzma.open('')
```

```
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: module 'lzma' has no attribute 'open'
```

### Буфер вывода

Пример из документации: 

```python
>>> import sys
>>> def flush():
...     print('flush', file=sys.stderr)
...     sys.stderr.flush()
...
>>> with open('out.txt', 'w') as f:
...     sys.stdout = f
...     print('hello', flush=flush)
...
hello
flush
```

или просто `print('hello', file=f)`

Можно применить и просто через перенапр
