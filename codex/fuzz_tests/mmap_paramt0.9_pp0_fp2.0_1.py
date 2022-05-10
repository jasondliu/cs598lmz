import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'XXX')
    m.seek(0)
    print(m.read(3))

with open('test', 'rb') as f:
    print(f.read())
```
Which produces the output

```
XXXb'XXX'
```

We can finalize this example by looking into the `mmap.ACCESS_*` constants and using `os.SEEK_SET` to set the mmap's offset.

### Bytes Support

`ugmp` supports bytes more strongly than `numpy` by having the flag `c.b` and having each "bytes" type be its own value. It can be used to create numpy arrays of bytes with
```python
>>> b = numpy.array([1,2,3], dtype=c.b)
>>> b
array([1, 2, 3], dtype=c.b)

>>> b.dtype
dtype(c.b)
```

And can be used with mmap with `os.SEEK_
