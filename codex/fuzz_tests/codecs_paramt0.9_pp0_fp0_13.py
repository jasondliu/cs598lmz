import codecs
codecs.register_error('replacer', encoding_replacer)

import sys, reprlib, os
if 'unicode' not in reprlib.get_repr_modules():
    from .repr import UnicodeRepr
else:
    UnicodeRepr = None

def configure():
    """
    Configure Strings for the current interpreter process.
    
    :return: None
    """
    default_encoding = sys.getdefaultencoding()
    default_error = sys.getfilesystemencoding()

    if UnicodeRepr is not None:
        import __builtin__
        __builtin__.repr = UnicodeRepr(lambda o: isinstance(o, strings.Unicode),
                                       unicode)
        sys.stdout = codecs.getwriter(default_encoding)(sys.stdout, 
                                                        errors=default_error)
        sys.stderr = codecs.getwriter(default_encoding)(sys.stderr, 
                                                        errors=default_error)
    encoding = default_encoding
    try:
        encoding = os.environ
