import codecs
codecs.register_error('xmlcharrefreplace', lambda e: (u''.join(unichr(0xFFFD)), e.end))


def encode_for_xml(unicode_data, encoding='ascii'):
    """
    Encode unicode_data for use as XML or HTML, with characters outside
    of the encoding converted to XML numeric character references.
    """
    return unicode_data.encode(encoding, 'xmlcharrefreplace')


def bytes_to_unicode(bytes, encoding='utf-8'):
    """
    Decode a str-type object (byte string) of the given encoding,
    raising a RaxaError if not possible.
    """
    try:
        return bytes.decode(encoding)
    except UnicodeDecodeError, e:
        raise TaxiiError('Unable to decode byte string into unicode string: %s' % str(e))
