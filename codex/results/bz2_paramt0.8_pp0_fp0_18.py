from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(archive)
 
import gzip
file = gzip.open(archive, mode='rb')
file.read()
 
# gzip.open() has a .read() method that works like other file objects
file.read(1024)
 
import zipfile
z = zipfile.ZipFile(archive, mode='r')
z.extractall()
len(z.namelist())
z.extract(z.namelist()[0])
 
# unzip.ZipFile has a close() method, plus a .namelist() method that lists the files in the archive, and an extract() method that extracts a file

# Use pip to install third-party packages that aren't in the Anaconda distribution
# Use the Anaconda distribution to install packages that aren't in pip
# The Anaconda distribution is a large collection of Python packages
# Some packages are available on PyPI, but not in Anaconda
# Some packages are available in Anaconda, but not on PyPI
# You can have pip and Anaconda installed at the same time, but it's easier to just use Anac
