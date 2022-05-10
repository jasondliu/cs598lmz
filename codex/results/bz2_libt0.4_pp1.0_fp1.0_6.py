import bz2
bz2.decompress(compressed_data)

# You can also use a context manager to automatically close the file
# at the end of the block, even if an exception occurs.
with bz2.BZ2File('file.bz2') as f:
    data = f.read()

# The compress() and decompress() functions produce and consume
# bytes objects. You can use a binary mode file like above or use
# the io.BytesIO() class to create a file-like interface to
# work with bytes objects.
import io

# Wrap a file, socket, or other binary data stream with a BZ2
# compressor object.
output = io.BytesIO()
with bz2.BZ2File(output, 'w') as compress:
    compress.write(original_data)

# Retrieve the compressed data.
compressed_data = output.getvalue()

# Wrap a file, socket, or other binary data stream with a BZ2
# decompressor object.
data = bz2.decompress(compressed_data)

# The compresslevel argument controls
