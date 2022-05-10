from bz2 import BZ2Decompressor
BZ2Decompressor()
#
# dirty hack to have bz2 working in python 2.7.6
#
import bz2
import sys
if sys.version_info[1] == 7:
    def _compress(self, data):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if isinstance(data, unicode):
            try:
                data = data.encode('utf-8')
            except UnicodeEncodeError:
                return bz2.BZ2Compressor.compress(self, data)
        return bz2.BZ2Compressor.compress(self, data)
    bz2.BZ2Compressor.compress = _compress

def import_data(filename='schema.sql.bz2',db_name=None):
    # read sql data
    if isinstance(filename, basestring):
        f = bz2.BZ2File(filename)
        sql_data = f.read()
        f.close()
    else:
        sql_data = filename.read()
