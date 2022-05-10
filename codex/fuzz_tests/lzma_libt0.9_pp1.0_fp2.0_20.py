import lzma
lzma.open(file_path)
</code>
not work?
This is a working example
<code>from lzma import open as lz_open
from tempfile import TemporaryDirectory, NamedTemporaryFile

tmp_d = TemporaryDirectory()
tmp_f = NamedTemporaryFile(suffix='.xz', dir=tmp_d.name, delete=False)
with lz_open(tmp_f.name, mode='w') as lz_f:
    lz_f.write(b'foobar')
lz_f.close()
with lz_open(tmp_f.name, mode='r') as lz_f:
    print(lz_f.read(5))
lz_f.close()
</code>

