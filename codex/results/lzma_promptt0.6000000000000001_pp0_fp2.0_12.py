import lzma
# Test LZMADecompressor
# TODO: use io.BytesIO instead of tempfile

# compress some data
data = b'1234567890' * 1000
compressed = lzma.compress(data)

# write it to a temporary file
import tempfile
with tempfile.TemporaryFile() as tmpfile:
    tmpfile.write(compressed)

    # seek back to the beginning, and decompress
    tmpfile.seek(0)
    d = lzma.LZMADecompressor()
    result = d.decompress(tmpfile.read())
    assert result == data
# Test LZMADecompressor.decompress() with multiple chunks

# compress some data
data = b'1234567890' * 1000
compressed = lzma.compress(data)

# write it to a temporary file
import tempfile
with tempfile.TemporaryFile() as tmpfile:
    tmpfile.write(compressed)

    # seek back to the beginning, and decompress
    tmpfile.seek(0)
    d = lzma.LZM
