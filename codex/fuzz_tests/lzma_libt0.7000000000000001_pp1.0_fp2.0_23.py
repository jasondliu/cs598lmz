import lzma
lzma.open('filename.xz')  # Open an XZ file.
```

Takes the same arguments as `open()`, and should be a complete replacement.

### 7-Zip Compression

The 7-Zip is a file archiver with highest compression ratio. The 7-zip project was started in 1999 by a Russian freelance programmer who is the developer and maintainer of this project.

```python
>>> import libarchive
>>> with libarchive.file_reader('test.7z') as e:
...     for entry in e:
...         with entry.get_file() as f:
...             for block in f:
...                 print block
...
>>>
```

**Compression**

```python
>>> import libarchive
>>> with libarchive.file_writer('test.7z', '7zip', format='7zip') as archive:
...     archive.add_files('/path/to/file1', '/path/to/file2', '/path/to/file3')
...
```

You can add files and directories, and specify the compression format to use.
