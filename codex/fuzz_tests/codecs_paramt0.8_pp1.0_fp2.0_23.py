import codecs
codecs.register_error('skip', lambda x: (u'?', x.start + 1))
ENCODING = 'utf-8'

def isascii(s):
    try:
        s.encode('ascii')
        return True
    except UnicodeDecodeError:
        return False

def get_unicode(s):
    try:
        return s.decode('ascii')
    except UnicodeDecodeError:
        return unicode(s, ENCODING, 'skip')

# Hacked version of json.dump to avoid crash on unicode characters.
def print_unicode(s):
    """Returns a python string that can be written to a json file.

    """
    try:
        s.decode('ascii')
        return s
    except UnicodeDecodeError:
        return s.encode(ENCODING)

def dump(obj, fp, skipkeys=False, ensure_ascii=True):
    """Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
    ``.write()``-supporting file-
