import lzma
# Test LZMADecompressor Class
data = b"X" * 100 + lzma.compress(b"Y" * 100)
with lzma.open(io.BytesIO(data), "rb") as f:
    print(f.read())

with io.BytesIO() as buf, lzma.open(buf, "wb") as f:
    f.write(b"adding this text to file")
    print(buf.getvalue())

with io.BytesIO(data) as src, io.BytesIO() as dst:
    with lzma.open(src) as f_in, lzma.open(dst, "w") as f_out:
        shutil.copyfileobj(f_in, f_out)
        data = dst.getvalue()
    print(data)

with io.BytesIO() as buf, lzma.open(buf, "w") as f:
    f.write(b"adding this text to file")
    print(buf.getvalue())

with io.BytesIO() as buf, lzma.open(buf, mode
