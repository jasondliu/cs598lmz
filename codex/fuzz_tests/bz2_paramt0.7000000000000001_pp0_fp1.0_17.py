from bz2 import BZ2Decompressor
BZ2Decompressor.__init__ = lambda *args, **kwargs: None
from io import BytesIO
BytesIO.__init__ = lambda *args, **kwargs: None
from subprocess import Popen, PIPE
Popen.__init__ = lambda *args, **kwargs: None
Popen.communicate = lambda *args, **kwargs: (b'', b'')
from urllib import request, parse
request.urlretrieve = lambda *args, **kwargs: None
request.install_opener = lambda *args, **kwargs: None
request.build_opener = lambda *args, **kwargs: None
request.build_opener.addheaders = lambda *args, **kwargs: None
request.build_opener.open = lambda *args, **kwargs: None
parse.urlparse = lambda *args, **kwargs: None
from xml.etree import ElementTree
ElementTree.parse = lambda *args, **kwargs: None
from xml.etree.ElementTree import Element
Element.findall = lambda *args, **kwargs: None
from xml.et
