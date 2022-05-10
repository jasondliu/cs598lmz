import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogateescape)

def open(filename, mode='r', encoding='utf-8', errors='surrogate_or_strict',
         newline=None):
    """open(filename, mode='r', encoding='utf-8', errors='surrogate_or_strict',
           newline=None) -> file object

    Open a file using the given mode and return a corresponding file object.
    Encoding defaults to 'utf-8'.  errors can be 'strict', 'ignore',
    'replace', 'surrogateescape' or 'surrogate_or_strict' (the default).
    newline can be None, '', '\n', '\r', and '\r\n'.  It works as
    specified in Python's open() builtin.

    The returned file object is wrapped with an io.TextIOWrapper instance.
    """
    mode = mode.replace('b', '')
    if 'U' in mode:
        if 'r' in mode:
            mode = mode.replace('U
