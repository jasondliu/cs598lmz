from lzma import LZMADecompressor
LZMADecompressor.decompress(open('compressed_file.bin', 'rb').read()).decode()
</code>

To address the issue of LZMA files containing multiple data blocks, you can either read a single block at a time and concatenate the results, or use an <code>lzma.StreamReader</code> to get one chunk at a time:
<code>import io
import lzma

stream = lzma.open('compressed_file.bin', 'rb')

# this will give one chunk of data at a time
with open('compressed_file.bin', 'rb') as f:
    reader = lzma.StreamReader(f)
    chunks = []
    for chunk in reader:
        chunks.append(chunk)

data = b''.join(chunks)
</code>

