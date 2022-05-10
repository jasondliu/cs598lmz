import lzma
lzma.LZMADecompressor().decompress(bytes(data))
</code>
In that light, considering this code above there is solution to any common usage od "codecs" library.
Solution:
Just replace:
<code>import codecs
with codecs.open(filename, 'rb') as f:
    data = f.read()
</code>
With:
<code>import codecs
from io import IOBase
from pathlib import Path

def read_from_file(filename: Path, binary=False, encoding=None) -&gt; IOBase:
    with filename.open('rb') as bf:
        binary_content = bf.read()
    return binary_content if binary else codecs.decode(binary_content, encoding)

data = read_from_file(filename, binary=True)
</code>

