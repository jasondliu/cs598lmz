import ctypes
ctypes.cast(buf, ctypes.c_char_p)

# Then, we can pass this address to libc.
libc.puts(buf)
```

### `libc.malloc(ctypes.c_uint(0x68))`
This is used to allocate a chunk of memory. By default, the size of the chunk is equal to `0x21`.
```
python3 -c "print 'a' * 0x21" | ./vuln
aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
*** Error in `./vuln': corrupted double-linked list: 0x000055c9f561b301 ***
Aborted
```

script
```python
buf = libc.malloc(ctypes.c_uint(0x21))
libc.puts(buf)
```

### `libc.vuln()`
The important function that reads our input.
```python
libc.vuln()
```

### `libc.system(buf)`
Make the chunk (which is pointed by `buf`
