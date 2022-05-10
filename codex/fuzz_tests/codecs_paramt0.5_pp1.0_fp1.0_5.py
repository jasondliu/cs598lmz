import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _encode(data):
    if isinstance(data, unicode):
        return data.encode('utf8', 'strict')
    return data

def _decode(data):
    if isinstance(data, str):
        return data.decode('utf8', 'strict')
    return data

def _encode_dict(data):
    return dict([(_encode(key), _encode(value)) for key, value in data.items()])

def _decode_dict(data):
    return dict([(_decode(key), _decode(value)) for key, value in data.items()])

def _encode_list(data):
    return [_encode(value) for value in data]

def _decode_list(data):
    return [_decode(value) for value in data]

def _encode_tuple(data):
    return tuple(_encode_list(data))

def _decode_tuple(data):
    return tuple
