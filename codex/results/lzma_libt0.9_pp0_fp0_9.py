import lzma
lzma.LZMADecompressor().decompress(b'\x00\x00\x00\x00\x00\x04\x00\xfdX\xfd\xdf\xf6\x04\x00')
```

```bash
> python decompression.py
running decompressor... 
i am the flag!
```
