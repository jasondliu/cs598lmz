from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh9\xcb\xcf\x07\x00\x00\x01\x01\x80\x02\xff\xff\xff\xff\x00\x1d\x00?\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
# b'Hello'
```

It's a lot of work to write the C code and compile it into a binary module. The easiest way to get a C module up and running is to use an existing one. There are many great extensions already written, including libraries for compression, XML processing, and GUI programming.

### Pip and PyPI

The Python Package Index (PyPI) is a vast collection of third-party Python libraries. 

PyPI makes it easy to install Python modules with pip, a simple command-line tool:

```
$ pip install requests
Collecting requests
  Downloading requests-2.18.4-py2.py3-none-any.whl (88kB)
    100% |████████
