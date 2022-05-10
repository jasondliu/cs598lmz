import codecs
codecs.register(codeerror.lookup)

def getExtension(name):
    """Given the name of a file return its extension (everything
    after the first '.').  If the name has no extension, returns an
    empty string.
    """
    l = string.split(name, '.')
    if len(l) == 1:
        return ''
    else:
        return l[-1]

def fileHasExtension(name, ext):
    """Given the name of a file, returns true iff the file has the
    given extension.

    This is the same as:
    >>> import ossubprocess
    >>> ossubprocess.getExtension(name) == ext
    """
    return getExtension(name) == ext


class Iterator(object):
    """Iterator base class.  You must implement the next and end
    methods, which are called repeatedly 'for i in Iterator()' until
    they eventually return 1 (done) or 0.
    """
    def __iter__(self):
        """Return iterator.
        """
        return self
