import lzma
# Test LZMADecompressor
with lzma.open('data/enwik8') as f:
    with lzma.open('data/enwik9', 'wt') as g:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            g.write(chunk)
# Test LZMAFile
with lzma.open('data/enwik8') as f:
    with lzma.open('data/enwik9', 'wt') as g:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            g.write(chunk)
# Test LZMAFile with seek()
with lzma.open('data/enwik8') as f:
    f.seek(1024)
    data = f.read()
    if data[0] != 32 or data[-1] != 10:
        raise RuntimeError("test failed")
# Test LZMAFile with seek() and tell()
with lzma.open('data/enwik8') as f:
    f.seek(1024
