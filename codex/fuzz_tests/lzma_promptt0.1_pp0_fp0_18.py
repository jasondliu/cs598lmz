import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = b'.'
while True:
    # Feed data in piece by piece, until you have
    # all of the compressed data
    buf = input_file.read(1024)
    if not buf:
        break
    data += buf
    # Try to decompress the data we have so far,
    # if it raises an EOFError, we're done
    try:
        result = decompressor.decompress(data)
    except lzma.LZMAError:
        # Not enough data to decompress yet,
        # get more data
        continue
    # We have all the data, decompress it in one go
    data = decompressor.decompress(data)
    output_file.write(data)
    break

# Flush the decompressor, to ensure no data is lost
result = decompressor.flush()
output_file.write(result)

# Clean up
input_file.close()
