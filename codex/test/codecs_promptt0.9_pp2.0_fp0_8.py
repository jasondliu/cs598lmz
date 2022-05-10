import codecs
# Test codecs.register_error('sillycodec', codecs.silly_codec_error)

# Python 2/3 interop.
try:
    # Python 3.
    import urllib.error as urlerror
    import urllib.request as urlrequest
    import urllib.parse as urlparse
    import urllib.parse as urlunparse
except ImportError:
    # Python 2.
    import urllib2 as urlerror
    import urllib2 as urlrequest
    import urlparse
    import urlparse as urlunparse

# Support --original in Python 2.
try:
    basestring = basestring
except NameError:
    basestring = str

