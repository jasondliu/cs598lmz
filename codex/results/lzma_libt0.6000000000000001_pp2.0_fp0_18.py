import lzma
lzma.open = lzma.LZMAFile
import bz2
bz2.open = bz2.BZ2File
import gzip
gzip.open = gzip.GzipFile
import zipfile
zipfile.open = zipfile.ZipFile
import tarfile
tarfile.open = tarfile.TarFile
import tempfile
tempfile.mkdtemp = lambda *args, **kw: tempfile.tempdir
import os
os.urandom = lambda n: os.environ['PYTHONHASHSEED']
os.getenv = lambda k: os.environ.get(k, None)
os.getcwd = lambda: os.environ.get('PWD', '/')
os.getpid = lambda: os.environ.get('$', '0')
os.path.realpath = lambda path: path
os.path.abspath = lambda path: path
os.path.dirname = lambda path: path
os.path.basename = lambda path: path
os.path.split = lambda path: (path, '')
os
