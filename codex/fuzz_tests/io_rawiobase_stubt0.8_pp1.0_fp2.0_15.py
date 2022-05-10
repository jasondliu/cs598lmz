import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, n=-1):
        with open(self.name, 'rb') as f:
            return f.read(n)
    def readable(self):
        return True
    def seekable(self):
        return False

#register the reader with OGR
ogr.RegisterFileDriver(FileDriver(File))

#if you want to use it as a FileGDB driver, use this
ogr.RegisterDriver(FileDriver('FileGDB'))

#open data source with driver and some arguments
ds = ogr.Open('MyFile', 'FileGDB')
#do work with the datasource
</code>

