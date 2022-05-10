import mmap
# Test mmap.mmap.write_byte on unseekable files.
import os
import io
import mmap

fileno, fname = tempfile.mkstemp('', 'mmap_byte_')
try:
    with os.fdopen(fileno, 'r+b') as f:
        f.write(b'x' * 100)
        f.flush()
        with mmap.mmap(f.fileno(), 100, access=mmap.ACCESS_WRITE) as m:
            m.write_byte(b'A')
        with open(fname, 'rb') as f2:
            data = f2.read()
    self.assertEqual(data, b'A' + b'\x00' * 99)
finally:
    os.unlink(fname)


# Test mmap.mmap.write on unseekable files.
import os
import io
import mmap

fileno, fname = tempfile.mkstemp('', 'mmap_write_')
