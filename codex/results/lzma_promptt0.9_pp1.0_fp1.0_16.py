import lzma
# Test LZMADecompressor:
c = lzma.LZMADecompressor()
c.decompress(data)
print(c.flush())
print(c.unused_data)

# Test LZMADecompressor with file objects:
with lzma.open("trylzma.txt.xz", "rb") as f:
    assert f.read() == data
    assert f.read(len(data)) == b""
with lzma.open("trylzma.txt.xz", "r") as f:
    assert f.read() == text
print("All test succeeded!")

# Bad LZMA format check
for size in [3, 4, 5, 8, 9]:
    data = b"x" * size
    try:
        lzma.decompress(data)
    except lzma.LZMAError as e:
        assert "(too short)" in str(e)
print("LZMAError format check succeeded!")

# Test decompressor readline()

def readtest(ctype, *args):
   
