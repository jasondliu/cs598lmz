from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

```
## Exercise 2:

**o** :::
**x** :::

```python
f = open(filename, 'w')
f.write(data)
f.close()
```

```python
with open(filename, 'w') as f:
    f.write(data)
```

문제점
- with 블록이 종료되면, f는 가비지 컬렉션의 대상이 된다.
- f에 close() 메서드가 호출되지 않는다.

## Exercise 3:

**o**
**x**

```python
chunk = iter(lambda: f.read(10), '')
```

```python
chunk = iter(partial(f
