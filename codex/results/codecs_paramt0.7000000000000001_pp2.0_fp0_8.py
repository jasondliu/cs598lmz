import codecs
codecs.register_error('strict', codecs.replace_errors)
codecs.register_error('replace', codecs.replace_errors)
codecs.register_error('surrogateescape', codecs.surrogateescape_error)
codecs.register_error('backslashreplace', codecs.backslashreplace_error)
codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_error)
codecs.register_error('namereplace', codecs.namereplace_error)


def _get_filesystem_encoding():
    '''Get the encoding used to convert Unicode filenames into system file
    names.'''
    encoding = sys.getfilesystemencoding()
    if encoding is None:
        encoding = sys.getdefaultencoding()
    return encoding


def _get_filesystem_errors():
    '''Get the error mode used to convert Unicode filenames into system file
    names.'''
    errors = sys.getfilesystemencodeerrors()
    if errors is None:
        errors = 'strict'
    return errors


