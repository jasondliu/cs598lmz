import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

class Py3Compat:
    """
    Compatibility layer for Python 3, which can be used in both Python 2 and Python 3.
    """

    def __init__(self):
        pass

    def is_python3(self):
        """
        Returns True if the current interpreter is Python 3.
        """
        return sys.version_info.major >= 3

    def is_python2(self):
        """
        Returns True if the current interpreter is Python 2.
        """
        return sys.version_info.major == 2

    def str_decode(self, str, encoding='utf-8'):
        """
        Decodes the given bytes to a string.
        """
        if self.is_python3():
            return str.decode(encoding, 'surrogateescape')
        else:
            return str

    def str_encode(self, str, encoding='utf-8'):
        """
        Encodes the given string to bytes.
        """
        if self.is_python
