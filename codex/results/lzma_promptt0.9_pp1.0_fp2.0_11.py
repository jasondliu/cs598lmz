import lzma
# Test LZMADecompressor
 
...
stream_reader = lzma.open('compressed_file.xz')
chunk_size = 4096
decompressor = lzma.LZMADecompressor()
 
while True:
    chunk = stream_reader.read(chunk_size)
    if len(chunk) == 0:
       break
 
    result = decompressor.decompress(chunk)
    if result:
      pass # do something
```

```python
import lzma
# Test LZMAFile
 
...
lzma_file = lzma.open('compressed_file.xz')
 
file_content = lzma_file.read()
lzma_file.close()
 
# Do something with the file content
```

### Multiple-file archives

```python
# <!--- We show an example of what NOT to do -->
import lzma
# Test LZMAFile for multiple-file archives
 
...
 
lzma_file = lzma.open('compressed
