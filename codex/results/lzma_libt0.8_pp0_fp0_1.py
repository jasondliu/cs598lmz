import lzma
lzma.decompress (os.urandom(24))

# Incorrect key
lzma.decompress (os.urandom(32))

# Incorrect key
lzma.decompress (os.urandom(15))

# Decoda from file-like object
lzma.decompress(in_file=StringIO(data))

# Decompress from file to file
lzma.decompress(in_file=StringIO(data), out_file=StringIO())
```

## Frequent Questions

### Why lzmaffi ?

lzmaffi provides an easy-to-use interface to the LZMA SDK.

### What is lzma ?

LZMA is a compression method first introduced in the 7-Zip program.
It gives a high compression rate (better than bzip2) and has a good decompression speed.

The LZMA SDK is written in ANSI C and is available under the Public Domain.

### What is python-lzma.dll ?

It's a DLL (Windows) or
