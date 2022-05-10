from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(g.get_by_id('/'+root).read())
 
```

This is exactly the same as in the previous task, except that the data is no longer encoded with `base64`, but with `bz2`. Fortunately, replacing the `base64` decoder with `bz2` is simple. `BZ2Decompressor` works like `io.BufferedIOBase` objects, which means we can pass it right into `tarfile.open`.
```python
with tarfile.open(mode='r|', fileobj=BZ2Decompressor().decompress(g.get_by_id('/'+root).read())) as tar:

    files = tar.getmembers()
    print(len(files))

    for member in files:
        if member.name.endswith('.dat'):
            print(member.name)
```

And again, the files seem to be numbered and are again all `400` by `400` pixels. 

## **Solve**

This task asks us to extract and follow the `400*
