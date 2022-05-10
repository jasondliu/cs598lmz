import lzma
# Test LZMADecompressor with default or bad preset value
with lzma.open("README.xz", "r") as f:
    try:
        f.read()
    except ValueError as e:
        print("ERROR: %s" % e)

with lzma.LZMADecompressor() as d:
    try:
        d.decompress(b'\x00')
    except ValueError as e:
        print("ERROR: %s" % e)

# Test LZMADecompressor with a negative preset value
with lzma.LZMADecompressor(preset=-1) as d:
    try:
        d.decompress(b'\x00')
    except ValueError as e:
        print("ERROR: %s" % e)

# Test LZMADecompressor with a preset value > 9
with lzma.LZMADecompressor(preset=10) as d:
    try:
        d.decompress(b'\x00')
    except ValueError as e:
        print
