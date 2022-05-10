import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _encode(s, encoding='utf-8'):
    return s.encode(encoding, 'strict')

def _decode(s, encoding='utf-8'):
    return s.decode(encoding, 'strict')

def _encode_or_decode(s, encoding='utf-8'):
    if isinstance(s, unicode):
        return _encode(s, encoding)
    else:
        return _decode(s, encoding)

def _encode_decode_list(l, encoding='utf-8'):
    return [_encode_or_decode(s, encoding) for s in l]

def _encode_decode_dict(d, encoding='utf-8'):
    return dict((_encode_or_decode(k, encoding), _encode_or_decode(v, encoding)) for k, v in d.iteritems())

def _encode_decode_tree(t, encoding='utf-8'
