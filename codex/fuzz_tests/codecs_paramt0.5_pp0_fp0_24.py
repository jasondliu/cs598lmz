import codecs
codecs.register_error('strict', codecs.ignore_errors)

__version__ = '0.8'

#-------------------------------------------------------------------------------

class Dict(dict):
    """A dictionary that allows for object-like property access syntax."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)
    def __setattr__(self, name, value):
        self[name] = value

def _to_unicode(s):
    if isinstance(s, unicode):
        return s
    if isinstance(s, basestring):
        try:
            return unicode(s, 'utf-8')
        except UnicodeDecodeError:
            return unicode(s, 'latin1')
    return unicode(s)

def _to_utf8(s):
    if isinstance(s, str):
        return s
    if isinstance(s, unicode):
        return s.encode('utf-8')
    return str(s)

def _to_
