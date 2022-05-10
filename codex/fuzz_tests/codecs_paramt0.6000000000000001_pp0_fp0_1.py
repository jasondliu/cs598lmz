import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _decode(s, encoding):
    return s.decode(encoding, 'strict')

def _encode(s, encoding):
    return s.encode(encoding, 'strict')

class PdfString(bytes):

    def __new__(cls, s, raw=False):
        self = bytes.__new__(cls, s)
        self._raw = raw
        return self

    def __repr__(self):
        return '%s(%s, raw=%s)' % (type(self).__name__, bytes.__repr__(self), self._raw)

    def __str__(self):
        if self._raw:
            return bytes.__str__(self)
        else:
            return _decode(bytes.__str__(self), 'latin1')

    def __unicode__(self):
        if self._raw:
            return _decode(bytes.__str__(self), 'raw')
        else:
            return _
