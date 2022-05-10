import lzma
lzma.compress(b"a" * 10)

import gzip
from io import BytesIO
filelike_object = BytesIO()
with gzip.GzipFile(fileobj=filelike_object, mode="w") as f:
    f.write(b"Hello\n")

