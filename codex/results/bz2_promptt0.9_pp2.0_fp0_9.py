import bz2
# Test BZ2Decompressor as a stateless stream filter by decompressing
# individual small chunks of data at a time.

import bz2

inp = b''
outp = b''
with open('testtar.tar.bz2', 'rb') as f:
	inp = f.read()
with bz2.BZ2File('testtar.tar.bz2', 'rb', buffering = 0) as f:
	outp = f.read()

print(inp ==ou
