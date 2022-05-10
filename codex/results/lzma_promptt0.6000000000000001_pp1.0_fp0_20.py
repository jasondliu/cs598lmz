import lzma
# Test LZMADecompressor by feeding it bytes and compare the result to the
# reference implementation xz.
#
# The data is compressed with xz using the same options as used in
# test_lzmaffi.py.

# Generate a random test case.
data = os.urandom(131072)

# Compress the test case with xz.
data_xz = subprocess.check_output(["xz", "-c", "--lzma2=preset=9,dict=64KiB"],
                                  input=data)

# Compress the test case with Python.
c = lzma.LZMACompressor(preset=9, dict_size=65536)
data_py = c.compress(data) + c.flush()

# Decompress the test case with xz.
data_xz_out = subprocess.check_output(["xz", "-cd"], input=data_xz)

# Decompress the test case with Python.
d = lzma.LZMADecompressor()
data_py_out =
