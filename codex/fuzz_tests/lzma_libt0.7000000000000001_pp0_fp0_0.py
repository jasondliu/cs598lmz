import lzma
lzma.LZMADecompressor()

import urllib.request

try:
    import ssl
except ImportError:
    _have_ssl = False
else:
    _have_ssl = True

__all__ = ["urlopen", "Request", "install_opener", "build_opener",
           "pathname2url", "url2pathname", "urlretrieve", "urlcleanup",
           "URLopener", "FancyURLopener", "proxy_bypass_macosx_sysconf"]

_opener = None

def _parse_proxy(proxy):
    """Parses the proxy URL into the scheme, user, password, host and port.
    Returns a 5-tuple: (scheme, user, password, host, port). All tuple
    elements are strings, and port is a string containing an integer.
    Returns None for missing or invalid proxy.
    """
    proxy = proxy or ''
    if not proxy:
        return None
    scheme, r_scheme = splittype(proxy)
    if not r_sche
