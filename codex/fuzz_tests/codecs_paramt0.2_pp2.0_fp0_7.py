import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _util

from . import _compat
from ._compat import PY2, PY3, text_type, binary_type, string_types, \
    urlparse, urlunparse, urlencode, urljoin, quote, unquote, \
    parse_qsl, parse_qs, urlsplit, urlunsplit, urlopen, \
    HTTPError, URLError, quote_plus, unquote_plus, \
    StringIO, BytesIO, OrderedDict, \
    HTTPConnection, HTTPSConnection, HTTPHandler, HTTPSHandler, \
    build_opener, install_opener, ProxyHandler, \
    Request, BaseHandler, HTTPRedirectHandler, \
    HTTPCookieProcessor, CookieJar, \
    parse_http_list, getproxies, proxy_bypass, \
    quote as _quote, unquote as _unquote, \
    urlparse as _urlparse, urlunparse as _urlunparse, \
    urlencode as _urlen
