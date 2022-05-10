from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#gz
import gzip
gzip.decompress(data)

#zip
from zipfile import ZipFile
ZipFile('example.zip').extractall()


#file obj
from cStringIO import StringIO

#写入
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print f.getvalue()

#读取
f = StringIO('Hello\nHi\nGoodbye')
while True:
    s = f.readline()
    if s == '':
        break
    print s.strip()

#流式处理
import sys

class RedirectStdoutTo(object):
    def __init__(self, out_new):
        self.out_new = out_new
    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new
    def __exit__(self, *args):
        sys.stdout =
