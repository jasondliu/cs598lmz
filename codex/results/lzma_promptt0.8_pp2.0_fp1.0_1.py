import lzma
# Test LZMADecompressor object
decompressor = lzma.LZMADecompressor()
with open("test.xz", "rb") as input, open("test", "wb") as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))
# Test highest_protocol
import pickle
import os.path

with open("test2.xz", "w+b") as f:
    pickle.dump(range(2000), f, pickle.HIGHEST_PROTOCOL)
    assert f.tell() == os.path.getsize("test2.xz")
# Test fileno
import os
import io

os.dup(io.open("test.xz", "rb").fileno())
# Test MemoryIO, BytesIO
import io
import lzma

with open("test.xz", "rb") as f:
    data = f.read()

assert lzma.decompress(io.BytesIO(data
