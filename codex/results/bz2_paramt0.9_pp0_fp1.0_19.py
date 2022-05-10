from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data[100:284])

from gzip import compress,decompress as gzip_decompress
with open('/tmp/test.txt','w')as f:
f.write(compress('日志压缩测试！'.encode('utf-8')))
with open('/tmp/test.txt','rb')as f:
g=f.read()
gzip_decompress(g).decode('utf-8')
from bz2 import compress as bz2_compress
with open('/tmp/test.txt','w') as f:
f.write(bz2_compress('日志压缩测试！'.encode('utf-8')))
with open('/tmp/test.txt','rb')as f:
g=f.read()
from bz2 import decompress
decompress(g).decode('utf-8')
from zlib import compress,decompress
with open('/tmp/test.txt','wb') as f:
