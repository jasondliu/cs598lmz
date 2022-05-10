from lzma import LZMADecompressor
LZMADecompressor().decompressobj(
    format=FORMAT_XZ,  # FOAMAT_ALONE_XZ to decompress a single file (MUST be the first argument)
).decompress(BZIP2_STREAM)

b'O, World!'
```

**Note:** LZMA file format is overly complicated. I tried to implement it, but it was a lot of work, and then I realized that there is no practical application of it. If you disagree - open an issue and tell me why.

### Building

```shell
python setup.py build [--xz] [--lzma]
```

If you want to **include bindings to liblzma** add the `--xz` or the `--lzma` flag, otherwise, only the python-only implementation will be built.

You may have to provide the location of the liblzma.a library and its header files:

```shell
python setup.py build --liblzma-a=lib/liblzma.a --liblzma-include=lib/liblz
