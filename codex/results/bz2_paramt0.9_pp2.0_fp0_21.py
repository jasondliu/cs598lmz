from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

len(BZ2Decompressor().decompress(data))

#: Web pages are normally compressed using GZip
from gzip import GzipFile
ftp = urlopen('http://www.python.org')
file = GzipFile(fileobj=BytesIO(ftp.read()))
content = file.read()

#: Or compressed using Bzip2
from bz2 import BZ2File
ftp = urlopen('http://www.python.org')
file = BZ2File(fileobj=BytesIO(ftp.read()))
content = file.read()

#: ## HTTP
#:
#: The HTTP protocol provides a Web service. We'll look at some of the
#: core elements of getting data from Web servers.
#:
#: ### The Web Client
#:
#: use *http.client*
#:
#: The *http.client* module provides methods for accessing Web resources. It
#: does not have convenience methods to get a particular page, so we need to use
#: the underlying building blocks in
