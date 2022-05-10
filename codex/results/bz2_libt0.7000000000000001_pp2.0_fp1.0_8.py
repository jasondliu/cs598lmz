import bz2
bz2.BZ2File('ex2.bz2', 'rb').read()

from gzip import GzipFile
from StringIO import StringIO

data = 'Two lines\n'

with GzipFile(fileobj=StringIO(data)) as f:
    print f.read()

with GzipFile(fileobj=StringIO(data), mode='w') as f:
    f.write(data)

from tempfile import TemporaryFile

with TemporaryFile() as temp:
    temp.write('Some data')
    temp.seek(0)
    print temp.read()

from tempfile import NamedTemporaryFile

with NamedTemporaryFile() as temp:
    print temp.name

from tempfile import mkstemp

file_handle, file_name = mkstemp()
with open(file_name, 'w') as f:
    f.write('This is some data')

import os
os.close(file_handle)
os.unlink(file_name)

from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_
