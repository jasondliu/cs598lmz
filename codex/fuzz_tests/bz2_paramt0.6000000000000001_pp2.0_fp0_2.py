from bz2 import BZ2Decompressor
BZ2Decompressor()

from gzip import GzipFile
GzipFile()

from zlib import decompressobj
decompressobj()

from cPickle import loads, dumps, HIGHEST_PROTOCOL
dumps(loads(dumps("string", HIGHEST_PROTOCOL)), HIGHEST_PROTOCOL)

from pickle import loads, dumps, HIGHEST_PROTOCOL
dumps(loads(dumps("string", HIGHEST_PROTOCOL)), HIGHEST_PROTOCOL)

from cStringIO import StringIO
StringIO()

from StringIO import StringIO
StringIO()

from xmlrpclib import ServerProxy
ServerProxy("http://localhost:8000/")

from urllib2 import urlopen
urlopen("http://www.python.org")

from xml.dom.minidom import parse
parse("/etc/passwd")

from ftplib import FTP
FTP("ftp.debian.org")

from hashlib import md5
md5("test message").hexdigest()

from hmac import HMAC

