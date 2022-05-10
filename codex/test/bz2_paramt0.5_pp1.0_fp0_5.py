from bz2 import BZ2Decompressor
BZ2Decompressor

import sys

# Python 2/3 compatibility
if sys.version_info.major == 2:
    import Queue as queue
    from urllib2 import urlopen
    from urllib2 import HTTPError
    from urllib import quote_plus
else:
    import queue
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from urllib.parse import quote_plus

