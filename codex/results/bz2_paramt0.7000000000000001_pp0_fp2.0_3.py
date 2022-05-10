from bz2 import BZ2Decompressor
BZ2Decompressor()

from gzip import GzipFile
GzipFile(fileobj=open('foo.gz', 'rb'), mode='rb')

from tarfile import TarFile
TarFile('foo.tar', mode='r', fileobj=open('foo.tar', 'rb'))

from zipfile import ZipFile
ZipFile('foo.zip')
ZipFile('foo.zip', mode='r')

from csv import DictReader
DictReader(open('foo.csv', 'rb'))

from csv import DictWriter
DictWriter(open('foo.csv', 'wb'), [])

from csv import reader
reader(open('foo.csv', 'rb'))

from csv import writer
writer(open('foo.csv', 'wb'))

from csv import Sniffer
Sniffer().sniff(open('foo.csv', 'rb').readline())

from json import load
load(open('foo.json', 'rb'))

from json import JSONDecoder
JSONDecoder().decode(open('foo.json', 'rb').read())
