import mmap
# Test mmap.mmap.flush
import os
import tempfile

def test_flush():
    with tempfile.TemporaryFile(mode='w+') as fp:
        fp.write("foobar")
        fp.flush()
        fp.seek(0)
        m = mmap.mmap(fp.fileno(), 0)
        m.flush()
        m.close()
