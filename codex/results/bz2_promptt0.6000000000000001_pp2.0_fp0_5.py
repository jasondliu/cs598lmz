import bz2
# Test BZ2Decompressor

from bz2 import BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
d = BZ2Decompressor()
d.decompress(data)
d.flush()
# Test BZ2File

from bz2 import BZ2File

with BZ2File('/tmp/foo.bz2', 'w') as f:
    f.write(b'hello world')

with BZ2File('/tmp/foo.bz2', 'r') as f:
    assert f.read() == b'hello world'

with BZ2File('/tmp/foo.bz2', 'r') as f:
    f.seek(5)
    assert f.tell() == 5
    assert f.read
