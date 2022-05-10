from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_ALONE).decompress(b'x\x9c+\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
b'hello'
```

## Additional notes:

* LZMA library is written in C, so it has limitations on 64-bit systems. It
  may not handle files larger than 2GB.

* LZMA library is written in ANSI C, so it has limitations on Windows systems.
  It may not handle filenames with unicode characters.

* If a user tries to read data from a stream before an EOF marker is reached,
  it raises an exception.  It's no longer legal for a user to read
  the stream past the end of an LZMA stream.

* The LZMA format of the wrapper + stream should be interoperable with
  the `xz` command-line tool.

* The LZMA format of the
