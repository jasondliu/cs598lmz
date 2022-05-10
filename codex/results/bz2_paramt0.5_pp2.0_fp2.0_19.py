from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# BytesIO
from io import BytesIO
buffer = BytesIO(b'\x00\x01\x02\x03\x04\x05')
buffer.read()
buffer.seek(0)
buffer.read()
buffer.write(b'\x06\x07\x08')
buffer.seek(0)
buffer.read()
buffer.close()

# StringIO
from io import StringIO
buffer = StringIO()
buffer.write('This is a test\n')
buffer.write('This is another test\n')
buffer.seek(0)
buffer.readline()
buffer.readline()
buffer.seek(0)
buffer.read()
buffer.close()

# mmap
import mmap

# tempfile
import tempfile
tempfile.mkstemp()
tempfile.mkdtemp()
fp = tempfile.TemporaryFile()
fp = tempfile.NamedTemporaryFile()
fp = tempfile.TemporaryFile(mode='w+t')
fp.name

