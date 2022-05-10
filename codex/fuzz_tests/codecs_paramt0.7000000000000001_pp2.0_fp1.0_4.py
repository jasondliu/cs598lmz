import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _recode(s, encodings):
    s = s.decode('utf-8', 'strict')
    for encoding in encodings:
        try:
            s = s.encode(encoding)
            break
        except UnicodeEncodeError:
            pass
    return s

def as_bytes(s, encodings=sys.getfilesystemencoding()):
    # try to encode s as a byte string but only use encodings that are
    # likely to be available on this system
    return _recode(s, [encodings, 'latin-1', 'utf-8'])

def _get_relpath(path, start=os.path.curdir):
    """Return a relative version of a path"""

    if not path:
        raise ValueError("no path specified")

    start_list = os.path.abspath(start).split(os.path.sep)
    path_list = os.path.abspath(path).split(os.path.
