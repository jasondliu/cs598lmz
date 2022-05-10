import mmap
# Test mmap.mmap for version > 0.7.6
# If version is < 0.7.6, use mmapfile instead
#try:
#    from mmap import mmap
#except ImportError:
#    from mmapfile import mmap

from cStringIO import StringIO
from csv import reader

from bz2 import BZ2File

def getheader(filename):
    """Get the header of a CSV-like file.

    :param filename: name of the CSV file
    :return: header as a list of strings
    """
    header = []
    if filename.endswith('.bz2'):
        fileobj = BZ2File(filename, 'rb')
    else:
        fileobj = open(filename, 'rb')
    for line in fileobj:
        if line.startswith('#'):
            continue
        elif line.startswith('"'): # GnuCash CSV reports
            delimiter = ','
        else:
            delimiter = '\t'
        header = line.split(delimiter)
        break
   
