import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Python 2 compatibility
if sys.version_info[0] < 3:
    import cPickle as pickle
    from cStringIO import StringIO
    from urllib2 import urlopen
    from urllib2 import Request as UrlRequest
    from urllib import urlencode as url_encode
    from urlparse import urljoin
    from urlparse import urlparse
    from urllib import quote as url_quote
    from urllib import unquote as url_unquote
    from urllib import quote_plus as url_quote_plus
    from urllib import unquote_plus as url_unquote_plus
    from urllib import urlencode
    import ConfigParser as configparser
    from itertools import izip_longest as zip_longest
    from itertools import izip as zip
    from itertools import imap as map
    from itertools import ifilter as filter
    from itertools import chain
    from collections import MutableMapping as DictMixin

