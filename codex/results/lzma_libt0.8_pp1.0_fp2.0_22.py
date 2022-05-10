import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

if sys.version_info < (3,):
    def b(s):
        return s

    def u(s):
        return unicode(s, 'unicode_escape')

    import cPickle as pickle

    class _Dummy(object):

        def __contains__(self, _):
            return False
        __iter__ = __contains__

        def items(self):
            return []
        iteritems = items

        def values(self):
            return []
        itervalues = values

        def keys(self):
            return []
        iterkeys = keys

    from urllib import (
        quote as url_quote,
        unquote as url_unquote,
        quote_plus as url_quote_plus,
        unquote_plus as url_unquote_plus,
        urlencode as url_encode,
        getproxies as getproxies_environment,
    )
    from urlparse import
