import codecs
# Test codecs.register_error for non-error raising actions.

encode_map = codecs.make_encoding_map({'source_char':'target_char',
                                       '\xe9': 'e',
                                       'a': None})

EXCEPTION = 'exception'

def encode_error(errors, encoding, error, ue):
    return (u'\ufffd', len(ue.object[ue.start:ue.end]))

def encode_create_map(errors, encoding, error, ue):
    return (int(ue.object[ue.start:ue.end]), len(ue.object[ue.start:ue.end]))

def encode_encode_map(errors, encoding, error, ue):
    return (encode_map.get(ue.object[ue.start:ue.end], u'?'),
            len(ue.object[ue.start:ue.end]))

