import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, size = -1):
        return open(self.name, 'rb').read(size)
    def seek(self, offset, whence = io.SEEK_CUR):
        open(self.name, 'rb').seek(offset, whence)
    def tell(self):
        return open(self.name, 'rb').tell()
    def write(self, input):
        return open(self.name, 'wb').write(input)
    def close(self):
        open(self.name).close()

import os
from os.path import isfile, join
onlyfiles = [f for f in allfiles if isfile(join(path, f))]
#for i in onlyfiles:
#    path = os.path.join('/mos/content/archive_site/london2012/models', i)
#    print path

path = '/mos/content/archive_site/london2012/models'
data = {}
for root, dirs, files in os.
