import lzma
# Test LZMADecompressor
from io import BytesIO
# Test LZMADecompressor with file object

from test import support
# Get function reference
from test.support import bigmemtest
from test.support import run_unittest


def check_decompressor(decompressor, data, chunksize=1, limit=None):
    # Test decompressor by decompressing the given data using it.
    # Read the data in chunks of the given size from the decompressor
    # and concatenate them. If limit is not None (the default), append
    # None to the data at the given position.
    concatenated = []
    total_read = 0
    while True:
        if limit is not None and total_read == limit:
            concatenated.append(None)
        chunk = decompressor.decompress(data[total_read:total_read+chunksize])
        if not chunk:
            break
        concatenated.append(chunk)
        total_read += len(chunk)
    data = b"".join(concatenated)
    return data



