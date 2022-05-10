import bz2
# Test BZ2Decompressor.read()

try:
    bz2.BZ2Decompressor
except AttributeError:
    print("lskdjf")
    raise SystemExit

# Get a file with a predictable compression.
