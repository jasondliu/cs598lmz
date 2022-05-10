import codecs
codecs.register_error('surrogate_or_undefine', _surrogate_or_undefine)

SUSPECT_ENCODING_PROPERTY_NAME = 'suspect-encoding'
SafePropertyManager.register_property(SUSPECT_ENCODING_PROPERTY_NAME, 'safe')


def error_handling_encode(text, encoding=None, work_encoding='shift_jis'):

    text = unicode(text, work_encoding).encode(encoding, 'surrogate_or_undefine')

    # replace corrupted characters
    text = text.replace('?', ' ')

    return text


class Stream(object):
    '''
    The `Collector.obtain` returns this `Stream` object.
    The contents managed by the returned stream object is encoded in unicode internally.
    You should encode the string using the `translate` method in your class.
    The translate method is called for every class in the WritePlugins.
    '''

    def __init__(self, title, body, path, encoding=
