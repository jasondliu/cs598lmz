import lzma
lzma.decompress(pp.get_payload(decode=True))

# more pipelining
import lzma
pp.get_payload(decode=True) | lzma.decompress()

# pipelining from stdin
import lzma
import sys
sys.stdin.buffer | lzma.decompress()

# pipelining to stdout
import lzma
import sys
sys.stdin.buffer | lzma.decompress() | sys.stdout.buffer.write()

# read_from and write_to functions
import lzma
with open('file.lzma', 'rb') as f:
    lzma.decompress(read_from=f.read)

import lzma
with open('file.xz', 'wb') as f:
    lzma.compress(b'...', write_to=f.write)

# write_to and read_from
import zlib
with open('file.gz', 'wb') as f:
    zlib.compress
